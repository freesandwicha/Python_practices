# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 4/9/2023 5:50 pm

#To make a python file which can automatically  email to a certain person.

import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials # The another file contains the credentials about my email.

def create_image_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
        return  mime_image

def send_image(to_email: str, subject: str, body: str, image: str | None = None ):
    host: str = 'smtp-mail.outlook.com'   # The format for sending hot/outlook email. Different emails for different formats.
    port: int = 587  #From the documentation

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('Logging in...')
        server.ehlo()  #Identify who we are.
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)

        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = credentials.EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        print('Sent!')


if __name__ == '__main__':
    send_image(to_email='*********@gmail.com',
               subject='Here is a test...',
               body='Hello!!!! I sent a picture to you.',
               image='*******.jpg')


