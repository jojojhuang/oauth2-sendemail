import smtplib
from email.mime.text import MIMEText
from email.header import Header
from oauth2 import get_oauth_string, get_oauth2_info

def sendmail(sender, receiver, msg, oauth2_info = get_oauth2_info()):

    message = MIMEText(msg['content'], 'html', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] =  Header(receiver['name'], 'utf-8')
    message['Subject'] = Header(msg['title'], 'utf-8')
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        auth_string = get_oauth_string(oauth2_info)
        server.ehlo(oauth2_info["google_client_id"])
        server.starttls()
        server.docmd("AUTH", "XOAUTH2 " + auth_string)

        server.sendmail(oauth2_info["email_address"], [receiver['email']], message.as_string())
        print('Have sended to {}'.format(receiver['email']))
    except smtplib.SMTPException as e:
        print(e)
