import argparse
import codecs
import sys
import tempfile
from pathlib import Path


DEFAULT_SOURCE = Path("식품_일반음식점.csv")
DEFAULT_OUTPUT = Path("식품_일반음식점_utf-8.csv")
SAMPLE_SIZE = 2 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024


def detect_encoding(source: Path) -> str:
    with source.open("rb") as file:
        sample = file.read(SAMPLE_SIZE)

    for bom, encoding in (
        (codecs.BOM_UTF32_LE, "utf-32"),
        (codecs.BOM_UTF32_BE, "utf-32"),
        (codecs.BOM_UTF8, "utf-8-sig"),
        (codecs.BOM_UTF16_LE, "utf-16"),
        (codecs.BOM_UTF16_BE, "utf-16"),
    ):
        if sample.startswith(bom):
            return encoding

    try:
        from charset_normalizer import from_bytes
    except ImportError as error:
        raise RuntimeError(
            "인코딩 자동 감지에는 charset-normalizer가 필요합니다. "
            "`uv sync`로 의존성을 설치하거나 "
            "`--source-encoding` 옵션으로 원본 인코딩을 지정하세요."
        ) from error

    match = from_bytes(sample).best()
    if match is None:
        raise RuntimeError(
            "원본 인코딩을 자동으로 감지하지 못했습니다. "
            "`--source-encoding` 옵션으로 지정하세요."
        )
    return match.encoding


def convert(source: Path, output: Path, source_encoding: str | None) -> str:
    if source.resolve() == output.resolve():
        raise ValueError("원본 파일과 결과 파일의 경로가 같습니다.")

    encoding = source_encoding or detect_encoding(source)
    decoder = codecs.getincrementaldecoder(encoding)(errors="strict")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            temporary_file.write(codecs.BOM_UTF8)
            with source.open("rb") as source_file:
                while chunk := source_file.read(CHUNK_SIZE):
                    temporary_file.write(decoder.decode(chunk).encode("utf-8"))
                temporary_file.write(decoder.decode(b"", final=True).encode("utf-8"))

        temporary_path.replace(output)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise

    return encoding


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CSV 파일의 문자 인코딩만 UTF-8로 변환합니다."
    )
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"원본 파일 (기본값: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"결과 파일 (기본값: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--source-encoding",
        help="원본 인코딩을 직접 지정합니다 (예: cp949, euc-kr, utf-8)",
    )
    args = parser.parse_args()

    try:
        encoding = convert(args.source, args.output, args.source_encoding)
    except (OSError, UnicodeError, LookupError, RuntimeError, ValueError) as error:
        print(f"변환 실패: {error}", file=sys.stderr)
        return 1

    print(f"변환 완료: {args.source} ({encoding}) -> {args.output} (UTF-8)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
