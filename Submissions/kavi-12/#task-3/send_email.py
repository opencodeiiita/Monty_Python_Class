# Importing the libraries
import  smtplib

# Initializing
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
# logging in own gmail account
import getpass
email = getpass.getpass('email:')
password = getpass.getpass('password: ')
smtp_obj.login(email,password)
# Receiver's address
send_add = input('receiver email address: ')

# Sending mail
from_add = email
to_add = send_add
subject = input('Subject:')
message = input('message:')
msg = 'Subject:' + subject + '\n' + message

smtp_obj.sendmail(from_add, to_add, msg)

