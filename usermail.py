import smtplib
import ssl
from email.message import EmailMessage

def send_mail(mail,user,id):
    from_email = 'dreamhomeaayush6@gmail.com'
    to_email = mail
    subject = "Welcome to our platform"
    message_template = "Dear {name},\n\nThank you for joining our platform.\nYour User Id is : {userid}.\nWe look forward to serving you.\n\nSincerely,\nTeam Dreamhome"

    message = message_template.format(name=user,userid=id)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    email_password = "ubvwoiqpxwxlwsqw"
    server.login(from_email, email_password)

    email_message = f'Subject: {subject}\n\n{message}'

    server.sendmail(from_email, to_email, email_message)

    server.quit()
