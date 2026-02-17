# Web Scraper

This script fetches Amazon search results and extracts product names and prices into a CSV file.

## How to run

1. Install dependencies:

```bash
python3 -m pip install requests beautifulsoup4
```

2. Run the script with a search query.

Example:

```bash
python3 script.py "wireless mouse" -o results.csv
```

### Notes

- Amazon pages can change and may block automated requests.
- Use this script responsibly and respect Amazon's terms of service.
