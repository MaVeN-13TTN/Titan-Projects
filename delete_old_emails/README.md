# Delete Old Emails Script

## Overview

This Python script connects to a Gmail account using IMAP and deletes emails older than 3 months from the inbox. It prompts the user for their Gmail address and app password and then performs the necessary operations.

## Prerequisites

- Python 3.x installed.
- Gmail account with "Less secure app access" enabled.
- IMAPlib library.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your_username/delete_old_emails.git
    cd delete_old_emails
    ```

2. **Install Dependencies:**
    ```bash
    pip install imaplib pytz
    ```

3. **Run the Script:**
    ```bash
    python delete_old_emails.py
    ```

4. **Enter Gmail Credentials:**
    - When prompted, enter your Gmail address and app password.

5. **Review Output:**
    - The script will display whether old emails were deleted successfully or if none were found.

## Notes

- Ensure "Less secure app access" is enabled in your Google Account settings.
- It's recommended to run the script in a secure environment.
- The script uses the IMAP protocol; make sure your firewall and security settings allow IMAP connections.

## Troubleshooting

- If you encounter issues, double-check your Gmail credentials and ensure your app password is correctly entered.
- Review Google's security settings for any blocks or warnings.

## Author

- Author: Ndung'u Kinyanjui
- Email: kinyanjuindungu1324@gmail.com
- GitHub: MaVeN-13TTN

