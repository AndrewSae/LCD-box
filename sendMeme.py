
import os
import random
import smtplib
import imghdr
from email.message import EmailMessage

email_address = 'EMAIL'
email_password = 'PASSWIRD'


def GetMeme():
    folder_directory = '/home/pi/LCD-box/memes'
    file_path = os.path.join(folder_directory, random.choice(os.listdir(folder_directory)))
    return file_path

def sendMeme():
    msg = EmailMessage()
    msg['Subject'] = "meme send test"
    msg['From'] = email_address
    msg['To'] = email_address
    msg.add_alternative("""/
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="app.css">
</head>
<body>
    <div id="header">
        <h1 id="headerTXT">Here is your meme as requested</h1>
    </div>
</body>
</html>
    """, subtype='html')


    with open (GetMeme(), 'rb') as img:
        file_data = img.read()
        file_type = imghdr.what(img.name)

    msg.add_attachment(file_data, maintype='image', subtype=file_type)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:


        smtp.login(email_address, email_password)
        smtp.send_message(msg)





