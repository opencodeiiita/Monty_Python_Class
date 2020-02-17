import smtplib

EmailId = input("Enter your email id")
Password = input("Enter your password")
Add = input("Enter reciever's email address")
Subject = input("Enter subject")
Message = input("Enter Message")
Email = 'Subject: {}\n\n{}'.format(Subject, Message)

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()


smtpObj.login(EmailId, Password)
smtpObj.sendmail(EmailId, Add, Email)
smtpObj.quit()
