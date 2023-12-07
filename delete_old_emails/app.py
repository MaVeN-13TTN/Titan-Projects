import imaplib
import email
from datetime import datetime, timedelta
from email.header import decode_header
from pytz import timezone
import getpass

# Constants
DAYS_THRESHOLD = 90

# Function to delete emails older than 3 months
def delete_old_emails(username, app_password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        # Connect to Gmail
        mail.login(username, app_password)
        mail.select("inbox")

        # Search for all emails in the inbox
        _, data = mail.search(None, "ALL")
        mail_ids = data[0].split()

        # Iterate through emails and delete those older than 3 months
        for mail_id in mail_ids:
            _, msg_data = mail.fetch(mail_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            # Decode the email subject to handle non-ASCII characters
            subject, encoding = decode_header(msg["Subject"])[0]
            subject = subject.decode(encoding or "utf-8") if isinstance(subject, bytes) else subject

            received_date_str = msg["Date"]

            # Remove the time zone offset string
            received_date_str = received_date_str.rsplit(' ', 1)[0]

            try:
                # Parse the received date string with the original format from Gmail
                received_date = datetime.strptime(received_date_str, "%a, %d %b %Y %H:%M:%S %z")
            except ValueError:
                # Handle unconverted data error by providing a default time and removing the time zone offset
                received_date_str = received_date_str.rsplit(' ', 1)[0] + ' 00:00:00'
                received_date = datetime.strptime(received_date_str, "%a, %d %b %Y %H:%M:%S")

            # Extract the time zone offset
            offset_str = msg["Date"].rsplit(' ', 1)[1]
            if '+' in offset_str or '-' in offset_str:
                offset_sign = -1 if offset_str.startswith('-') else 1
                offset_hours = int(offset_str[1:3])
                offset_minutes = int(offset_str[3:])
                offset = timedelta(hours=offset_sign * offset_hours, minutes=offset_sign * offset_minutes)
            else:
                offset = timedelta()

            # Adjust the received date with the time zone offset
            received_date = received_date - offset

            three_months_ago = datetime.now() - timedelta(days=DAYS_THRESHOLD)

            if received_date < three_months_ago:
                mail.store(mail_id, '+FLAGS', '(\Deleted)')

        # Expunge to permanently delete the marked emails
        mail.expunge()
        mail.close()
        mail.logout()

        # Provide user feedback
        if mail_ids:
            print("Old emails deleted successfully.")
        else:
            print("No emails older than 3 months found.")
    except imaplib.IMAP4.error as e:
        print(f"IMAP Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def get_gmail_credentials():
    # Prompt for Gmail username
    username = input("Enter your Gmail address: ")
    
    # Prompt for the app password
    app_password = getpass.getpass("Enter your Gmail app password: ")

    return username, app_password

if __name__ == "__main__":
    # Get Gmail credentials
    username, app_password = get_gmail_credentials()

    # Call the function to delete old emails
    delete_old_emails(username, app_password)
