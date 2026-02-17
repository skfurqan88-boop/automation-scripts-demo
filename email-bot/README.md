# Email Bot

This script sends personalized emails through Gmail SMTP. It reads a CSV file with `name` and `email` columns and sends a custom message to each recipient.

## How to run

1. Create an app password in your Google account and store credentials as environment variables:

```bash
export GMAIL_USER="you@gmail.com"
export GMAIL_APP_PASSWORD="your_app_password"
```

2. Prepare a CSV file (example: `recipients.csv`) with columns `name` and `email`.
3. Run the script:

```bash
python3 script.py recipients.csv "Hello" "Hi {name}, this is a test email."
```

### Notes

- Gmail requires an app password when 2-step verification is enabled.
- Use the `{name}` placeholder to personalize each message.
