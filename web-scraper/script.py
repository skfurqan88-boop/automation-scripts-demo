#!/usr/bin/env python3
"""Scrape product names and prices from Amazon search results."""

import argparse
import csv
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def build_search_url(query: str) -> str:
    params = urlencode({"k": query})
    return f"https://www.amazon.com/s?{params}"


def parse_results(html: str) -> List[Tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    results: List[Tuple[str, str]] = []

    for item in soup.select('div[data-component-type="s-search-result"]'):
        name_tag = item.select_one("h2 span")
        price_tag = item.select_one("span.a-price > span.a-offscreen")

        if not name_tag:
            continue

        name = name_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True) if price_tag else ""
        results.append((name, price))

    return results


def scrape_amazon(query: str) -> List[Tuple[str, str]]:
    url = build_search_url(query)
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=20)
    response.raise_for_status()
    return parse_results(response.text)


def write_csv(rows: List[Tuple[str, str]], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["product_name", "price"])
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scrape product names and prices from Amazon search results."
    )
    parser.add_argument("query", help="Search query, e.g. 'wireless mouse'")
    parser.add_argument(
        "-o",
        "--output",
        default="results.csv",
        help="Path for the output CSV file (default: results.csv)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)

    rows = scrape_amazon(args.query)
    write_csv(rows, output_path)
    print(f"Saved {len(rows)} results to {output_path}")


if __name__ == "__main__":
    main()
