#!/usr/bin/env python3
"""Send personalized emails using Gmail SMTP."""

import argparse
import csv
import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Dict


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def load_recipients(csv_path: Path) -> list[Dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        recipients = [row for row in reader]

    if not recipients:
        raise SystemExit("No recipients found in the CSV file.")

    return recipients


def send_emails(
    recipients: list[Dict[str, str]],
    sender: str,
    password: str,
    subject: str,
    message_template: str,
) -> None:
    context = ssl.create_default_context()

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(sender, password)

        for recipient in recipients:
            name = recipient.get("name", "there")
            email = recipient.get("email")
            if not email:
                continue

            message = EmailMessage()
            message["From"] = sender
            message["To"] = email
            message["Subject"] = subject
            message.set_content(message_template.format(name=name))

            server.send_message(message)
            print(f"Sent email to {name} <{email}>")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Send personalized emails from a CSV list using Gmail SMTP."
    )
    parser.add_argument("input", help="Path to CSV with 'name' and 'email' columns")
    parser.add_argument("subject", help="Email subject line")
    parser.add_argument(
        "message",
        help="Message template (use {name} for personalization)",
    )
    parser.add_argument(
        "--sender",
        default=os.getenv("GMAIL_USER", ""),
        help="Sender Gmail address (or set GMAIL_USER env var)",
    )
    parser.add_argument(
        "--password",
        default=os.getenv("GMAIL_APP_PASSWORD", ""),
        help="Gmail app password (or set GMAIL_APP_PASSWORD env var)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sender = args.sender.strip()
    password = args.password.strip()

    if not sender or not password:
        raise SystemExit(
            "Missing credentials. Provide --sender/--password or set "
            "GMAIL_USER and GMAIL_APP_PASSWORD."
        )

    csv_path = Path(args.input)
    if not csv_path.exists():
        raise SystemExit(f"Input file not found: {csv_path}")

    recipients = load_recipients(csv_path)
    send_emails(recipients, sender, password, args.subject, args.message)


if __name__ == "__main__":
    main()
