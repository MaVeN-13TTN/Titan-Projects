import imaplib
import email
from datetime import datetime, timedelta
from getpass import getpass
from email.header import decode_header

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
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            received_date = datetime.strptime(msg["Date"], "%a, %d %b %Y %H:%M:%S %z")
            three_months_ago = datetime.now() - timedelta(days=90)

            if received_date < three_months_ago:
                mail.store(mail_id, '+FLAGS', '(\Deleted)')

        # Expunge to permanently delete the marked emails
        mail.expunge()
        mail.close()
        mail.logout()
        print("Old emails deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Prompt for Gmail credentials
username = input("Enter your Gmail address: ")
app_password = getpass("Enter your Gmail app password: ")

# Call the function to delete old emails
delete_old_emails(username, app_password)




