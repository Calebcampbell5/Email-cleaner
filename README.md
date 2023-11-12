# Email-cleaner 
Python Script that I needed for maintaining Emails, I needed to clean my email inbox so I wrote this script to speed up that process. 

# Installation

``` pip install imaplib ```

``` pip install email ```

- This Python script has the necessary libraries and functions with Gmail's IMAP servers in mind code changes will need to be made if you are using a different email provider. 
# Usage:
- Modifiy the Function's arguments with your_email_address, your_password, and sender_email
```Python
delete_emails_from_sender('your_email_address', 'your_password', 'sender-email')
```
# Improvments
```python
  Print() 
```
- Print functions can be included to insure connection to IMAP Email server and the successful removal of emails.
