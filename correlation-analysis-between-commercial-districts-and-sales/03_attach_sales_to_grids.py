import argparse
import csv
import math
import sys
import tempfile
from pathlib import Path

from pyproj import Transformer
from pyproj.exceptions import ProjError


DEFAULT_SALES = Path("매출정보.csv")
DEFAULT_GRIDS = Path("격자배치결과.csv")
DEFAULT_OUTPUT = Path("격자매출배치결과.csv")
GRID_SIZE = 1000
SALES_COLUMN = "매출액"
X_COLUMN = "좌표정보(X)"
Y_COLUMN = "좌표정보(Y)"
GRID_X_COLUMN = "격자좌상단좌표정보(X)"
GRID_Y_COLUMN = "격자좌하단좌표정보(Y)"
GRID_ID_COLUMN = "격자ID"
RESTAURANT_COUNT_COLUMN = "음식점카운팅"
OUTPUT_COLUMNS = (SALES_COLUMN, GRID_ID_COLUMN, RESTAURANT_COUNT_COLUMN)


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


def load_grids(grid_path: Path) -> tuple[dict[tuple[int, int], tuple[str, str]], int, int]:
    grids = {}
    min_x = math.inf
    max_top_y = -math.inf

    with grid_path.open("r", encoding="utf-8-sig", newline="") as grid_file:
        reader = csv.DictReader(grid_file)
        required_columns = {
            GRID_ID_COLUMN,
            GRID_X_COLUMN,
            GRID_Y_COLUMN,
            RESTAURANT_COUNT_COLUMN,
        }
        missing_columns = required_columns.difference(reader.fieldnames or ())
        if missing_columns:
            raise ValueError(
                "격자 CSV에 필요한 열이 없습니다: "
                + ", ".join(sorted(missing_columns))
            )

        for line_number, row in enumerate(reader, start=2):
            try:
                x_left = int((row[GRID_X_COLUMN] or "").strip())
                y_bottom = int((row[GRID_Y_COLUMN] or "").strip())
                grid_id = (row[GRID_ID_COLUMN] or "").strip()
                restaurant_count = (row[RESTAURANT_COUNT_COLUMN] or "").strip()
                if not grid_id or not restaurant_count:
                    raise ValueError("격자 ID 또는 음식점 수가 비어 있습니다.")
            except (KeyError, ValueError) as error:
                raise ValueError(
                    f"격자 CSV의 {line_number}번째 행을 읽을 수 없습니다: {error}"
                ) from error

            key = (x_left, y_bottom)
            if key in grids:
                raise ValueError(
                    f"격자 CSV에 중복된 격자가 있습니다: X={x_left}, Y={y_bottom}"
                )
            grids[key] = (grid_id, restaurant_count)
            min_x = min(min_x, x_left)
            max_top_y = max(max_top_y, y_bottom + GRID_SIZE)

    if not grids:
        raise ValueError("격자 CSV에 격자 데이터가 없습니다.")

    return grids, int(min_x), int(max_top_y)


def attach_sales(sales_path: Path, grid_path: Path, output_path: Path) -> tuple[int, int, int]:
    if sales_path.resolve() == output_path.resolve():
        raise ValueError("매출 원본과 결과 파일의 경로가 같습니다.")
    if grid_path.resolve() == output_path.resolve():
        raise ValueError("격자 원본과 결과 파일의 경로가 같습니다.")

    grids, min_x, max_top_y = load_grids(grid_path)
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:5174", always_xy=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    input_rows = 0
    matched_rows = 0
    invalid_coordinates = 0

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8-sig",
            newline="",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as output_file:
            temporary_path = Path(output_file.name)
            writer = csv.writer(output_file)
            writer.writerow(OUTPUT_COLUMNS)

            with sales_path.open("r", encoding="utf-8-sig", newline="") as sales_file:
                reader = csv.DictReader(sales_file)
                required_columns = {SALES_COLUMN, X_COLUMN, Y_COLUMN}
                missing_columns = required_columns.difference(reader.fieldnames or ())
                if missing_columns:
                    raise ValueError(
                        "매출 CSV에 필요한 열이 없습니다: "
                        + ", ".join(sorted(missing_columns))
                    )

                for row in reader:
                    input_rows += 1
                    x = parse_coordinate(row.get(X_COLUMN))
                    y = parse_coordinate(row.get(Y_COLUMN))
                    if x is None or y is None or not -180 <= x <= 180 or not -90 <= y <= 90:
                        invalid_coordinates += 1
                        continue

                    projected_x, projected_y = transformer.transform(x, y)
                    if not math.isfinite(projected_x) or not math.isfinite(projected_y):
                        invalid_coordinates += 1
                        continue

                    column = math.floor((projected_x - min_x) / GRID_SIZE)
                    grid_row = math.floor((max_top_y - projected_y) / GRID_SIZE)
                    grid_key = (
                        min_x + column * GRID_SIZE,
                        max_top_y - (grid_row + 1) * GRID_SIZE,
                    )
                    grid = grids.get(grid_key)
                    if grid is None:
                        continue

                    writer.writerow(
                        (
                            (row.get(SALES_COLUMN) or "").strip(),
                            grid[0],
                            grid[1],
                        )
                    )
                    matched_rows += 1

        temporary_path.replace(output_path)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise

    return input_rows, matched_rows, invalid_coordinates


def main() -> int:
    parser = argparse.ArgumentParser(
        description="매출 좌표를 EPSG:5174 격자에 매칭합니다."
    )
    parser.add_argument(
        "sales",
        nargs="?",
        type=Path,
        default=DEFAULT_SALES,
        help=f"매출 CSV (기본값: {DEFAULT_SALES})",
    )
    parser.add_argument(
        "grids",
        nargs="?",
        type=Path,
        default=DEFAULT_GRIDS,
        help=f"격자 CSV (기본값: {DEFAULT_GRIDS})",
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
        input_rows, matched_rows, invalid_coordinates = attach_sales(
            args.sales, args.grids, args.output
        )
    except (OSError, UnicodeError, csv.Error, ValueError, ProjError) as error:
        print(f"배치 실패: {error}", file=sys.stderr)
        return 1

    unmatched_rows = input_rows - matched_rows - invalid_coordinates
    print(
        f"배치 완료: 매출 {input_rows:,}개 중 격자 매칭 {matched_rows:,}개, "
        f"좌표 오류 {invalid_coordinates:,}개, 격자 범위 밖 {unmatched_rows:,}개; "
        f"{args.output}에 저장했습니다."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
