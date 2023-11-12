import imaplib
import email
from email.header import decode_header

def delete_emails_from_sender(username, password, sender, folder="Inbox"):
    
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  

    mail.login(username, password)

    mail.select(folder)

    _, message_numbers = mail.search(None, f'(FROM "{sender}")')

    
    for num in message_numbers[0].split():
        mail.store(num, '+FLAGS', '(\Deleted)')

    mail.expunge()

    mail.logout()

if __name__ == "__main__":
    delete_emails_from_sender('your_email_address', 'your_password', 'sender_email')