import smtplib

email = input('')
password = input('')
subject = input('')
message = input('')
receiver_address = input('')

mail = 'Subject: {}\n\n{}'.format(subject, message)

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()


smtpObj.login(email, password)
smtpObj.sendmail(email, receiver_address, mail)
smtpObj.quit()