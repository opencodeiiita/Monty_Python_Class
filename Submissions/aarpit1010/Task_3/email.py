import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendemail(from,pass,to,subject,body):

msg=MIMEText(body)

msg['From']=from

msg['To']=to

msg['Subject']=subject
smtpserver=smtplib.SMTP('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(from,pass)
smtpserver.sendmail(from,to,msg.as_string())
smtpserver.close()
def main():
    from = raw_input('Enter your Gmail ID')
    pass =getpass.getpass()
    to =raw_input('Enter receiver mail ID')
    subject=raw_input('Enter Subject')
    body=raw_input('Enter Body')
    sendemail(from,pass,to,subject,body)
    if __name__=='__main__':
        main()
