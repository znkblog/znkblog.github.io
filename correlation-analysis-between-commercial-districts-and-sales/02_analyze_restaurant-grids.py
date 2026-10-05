import argparse
import csv
import math
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Iterator


DEFAULT_SOURCE = Path("식품_일반음식점_utf-8.csv")
DEFAULT_OUTPUT = Path("격자배치결과.csv")
GRID_SIZE = 1000
STATUS_COLUMN = "영업상태명"
X_COLUMN = "좌표정보(X)"
Y_COLUMN = "좌표정보(Y)"
ACTIVE_STATUS = "영업/정상"
OUTPUT_COLUMNS = (
    "격자ID",
    "격자좌상단좌표정보(X)",
    "격자좌상단좌표정보(Y)",
    "음식점카운팅",
)


def parse_coordinate(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        coordinate = float(value)
    except ValueError:
        return None
    return coordinate if math.isfinite(coordinate) else None


def iter_active_coordinates(
    source: Path,
) -> Iterator[tuple[float, float, bool]]:
    with source.open("r", encoding="utf-8-sig", newline="") as source_file:
        reader = csv.DictReader(source_file)
        required_columns = {STATUS_COLUMN, X_COLUMN, Y_COLUMN}
        missing_columns = required_columns.difference(reader.fieldnames or ())
        if missing_columns:
            raise ValueError(
                "CSV에 필요한 열이 없습니다: " + ", ".join(sorted(missing_columns))
            )

        for row in reader:
            if (row.get(STATUS_COLUMN) or "").strip() != ACTIVE_STATUS:
                continue

            x = parse_coordinate(row.get(X_COLUMN))
            y = parse_coordinate(row.get(Y_COLUMN))
            if x is None or y is None:
                yield 0.0, 0.0, False
            else:
                yield x, y, True


def analyze(source: Path, output: Path) -> tuple[int, int, int]:
    if source.resolve() == output.resolve():
        raise ValueError("원본 파일과 결과 파일의 경로가 같습니다.")

    min_x = math.inf
    max_x = -math.inf
    min_y = math.inf
    max_y = -math.inf
    active_rows = 0
    valid_coordinates = 0

    for x, y, valid in iter_active_coordinates(source):
        active_rows += 1
        if not valid:
            continue
        valid_coordinates += 1
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8-sig",
            newline="",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as output_file:
            temporary_path = Path(output_file.name)
            writer = csv.writer(output_file)
            writer.writerow(OUTPUT_COLUMNS)

            if valid_coordinates:
                left_x = math.floor(min_x / GRID_SIZE) * GRID_SIZE
                top_y = math.ceil(max_y / GRID_SIZE) * GRID_SIZE
                columns = math.floor((max_x - left_x) / GRID_SIZE) + 1
                rows = math.floor((top_y - min_y) / GRID_SIZE) + 1
                counts: defaultdict[tuple[int, int], int] = defaultdict(int)

                for x, y, valid in iter_active_coordinates(source):
                    if not valid:
                        continue
                    column = math.floor((x - left_x) / GRID_SIZE)
                    row = math.floor((top_y - y) / GRID_SIZE)
                    counts[(row, column)] += 1

                for row in range(rows):
                    top_left_y = top_y - row * GRID_SIZE
                    for column in range(columns):
                        top_left_x = left_x + column * GRID_SIZE
                        grid_id = f"G{row * columns + column + 1:06d}"
                        writer.writerow(
                            (
                                grid_id,
                                top_left_x,
                                top_left_y,
                                counts[(row, column)],
                            )
                        )

        if temporary_path is not None:
            temporary_path.replace(output)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise

    return active_rows, valid_coordinates, (rows * columns if valid_coordinates else 0)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="영업 중인 음식점 좌표를 1km 격자별로 집계합니다."
    )
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"입력 CSV (기본값: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"결과 CSV (기본값: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    try:
        active_rows, valid_coordinates, grid_count = analyze(args.source, args.output)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"분석 실패: {error}", file=sys.stderr)
        return 1

    invalid_coordinates = active_rows - valid_coordinates
    print(
        f"분석 완료: 영업/정상 {active_rows:,}개 중 좌표 유효 "
        f"{valid_coordinates:,}개, 제외 {invalid_coordinates:,}개; "
        f"격자 {grid_count:,}개를 {args.output}에 저장했습니다."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
