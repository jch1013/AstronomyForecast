from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

my_email = 'astroforecasttonight@gmail.com'


def create_message(destination, subject, body):
    message = MIMEText(body)
    message['to'] = destination
    message['from'] = my_email
    message['subject'] = subject
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, destination, subject, body):
    return service.users().messages().send(
      userId="me",
      body=create_message(destination, subject, body)
    ).execute()
