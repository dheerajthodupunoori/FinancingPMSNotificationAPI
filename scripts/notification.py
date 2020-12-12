import smtplib
from config.app_config import MAILCONFIG
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(mail_data):
    # Getting details for email
    sender_address = MAILCONFIG.sender_address
    pwd = MAILCONFIG.password
    mail_content = mail_data['Body']

    # preparing message
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = mail_data['ReceiverMailID']
    message['Subject'] = mail_data['Subject']
    message.attach(MIMEText(mail_content, 'plain'))

    # creating SMTP session
    session = smtplib.SMTP(MAILCONFIG.mail_server, MAILCONFIG.port)
    session.starttls()
    session.login(sender_address, pwd)
    text = message.as_string()
    session.sendmail(sender_address, mail_data['ReceiverMailID'], text)
    session.quit()
