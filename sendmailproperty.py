import smtplib
import ssl
from email.message import EmailMessage

def send_mailp(mail,user):
    from_email = 'dreamhomeaayush6@gmail.com'
    to_email = mail
    subject = "Property Registered"
    message_template = "Dear {name},\n\nThank you for registering your property on our platform.\nYour property is successfully registered.\nWe look forward to serve you.\n\nRegards,\nTeam Dreamhome"

    message = message_template.format(name=user)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    email_password = "ubvwoiqpxwxlwsqw"
    server.login(from_email, email_password)

    email_message = f'Subject: {subject}\n\n{message}'
    server.sendmail(from_email, to_email, email_message)

    server.quit()

