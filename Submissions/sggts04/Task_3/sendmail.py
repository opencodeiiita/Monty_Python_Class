import smtplib
import getpass

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = input('Your Email: ')
print('Your Password: ')
passwd = getpass.getpass()

smtp_obj.login(email, passwd)

send_add = input('Send email to? ')

subj = input('Subject: ')
mesg = input('Message: ')
msg = 'Subject:' + subj + '\n' + mesg

smtp_obj.sendmail(email, send_add, msg)
smtp_obj.quit()