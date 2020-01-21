import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = ''
passwd = ''

smtp_obj.login(email, passwd)

send_add = input('Send email to? ')

subj = input('Subject: ')
mesg = input('Message: ')
msg = 'Subject:' + subj + '\n' + mesg

smtp_obj.sendmail(email, send_add, msg)