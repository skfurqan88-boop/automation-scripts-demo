#!/usr/bin/env python3
"""Clean a CSV file by trimming whitespace and removing empty rows."""

import argparse
import csv
from pathlib import Path


def clean_csv(input_path: Path, output_path: Path) -> int:
    """Return the number of rows written after cleaning."""
    rows_written = 0

    with input_path.open(newline="", encoding="utf-8") as infile, output_path.open(
        "w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Trim whitespace from each cell and drop fully empty rows.
            cleaned = [cell.strip() for cell in row]
            if not any(cleaned):
                continue
            writer.writerow(cleaned)
            rows_written += 1

    return rows_written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean a CSV file by removing empty rows and trimming spaces."
    )
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument(
        "-o",
        "--output",
        default="output.csv",
        help="Path for the cleaned CSV file (default: output.csv)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    rows_written = clean_csv(input_path, output_path)
    print(f"Cleaned CSV saved to {output_path} ({rows_written} rows)")


if __name__ == "__main__":
    main()
