# Automation Scripts Demo

Portfolio repo showcasing Python automation scripts (Excel cleaner, web scraper, email bot).

## Scripts

- **Excel Cleaner**: Cleans a CSV file by trimming whitespace and removing empty rows.
- **Web Scraper**: Scrapes Amazon search results for product names and prices.
- **Email Bot**: Sends personalized emails from a CSV list using Gmail SMTP.

## How to run

1. Each folder contains its own `README.md` with setup and usage instructions.
2. Use Python 3 and install any required dependencies per script.

Quick examples:

```bash
# Excel cleaner
python3 excel-cleaner/script.py data.csv -o output.csv

# Web scraper
python3 web-scraper/script.py "wireless mouse" -o results.csv

# Email bot
python3 email-bot/script.py recipients.csv "Hello" "Hi {name}, this is a test email."
```