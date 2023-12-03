# Gmail Delete Old Emails Script

## Overview

This Python script allows you to delete emails older than 3 months from your Gmail account. It connects to the Gmail IMAP server, retrieves email information, and deletes messages that exceed the specified time threshold.

## Prerequisites

Before running the script, make sure you have the necessary dependencies installed. Use the following command to install them:

```bash
pip install imapclient secure-smtplib
```

## Usage

1. **Enable "Less secure app access" in your Google account settings.**
2. **Generate an "App Password"** in your Google account to use as the password in the script.
3. **Run the script:**

    ```bash
    python delete_old_emails.py
    ```

4. **Enter your Gmail address and app password** when prompted.

## Important Notes

- The script permanently deletes emails, so use it with caution.
- Ensure that your Gmail account settings allow less secure app access.
- Keep your app password secure and do not share it.

## Troubleshooting

If you encounter issues, check the following:

- **Correct Gmail credentials:** Ensure you provide the correct Gmail address and app password.
- **Dependencies:** Make sure you've installed the required dependencies (`imapclient` and `secure-smtplib`).

## Disclaimer

Use this script at your own risk. Understand the implications of permanently deleting emails and always keep backups of critical information.

**Author:** [Ndung'u Kinyanjui]

