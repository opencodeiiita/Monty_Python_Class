import smtplib
import getpass

# Connecting to Server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Getting User Credentials
userEmail = input("Enter your Email ID:")
userPass = getpass.getpass("Enter your Password:")

# Logging In
server.login(userEmail, userPass)
# Getting Receiver Email & Message
recieverEmail = input("Enter Reciever's Email ID:")

messageSubject = input('Enter Subject:')
messageBody = input('Enter Body:')
message = 'Subject:' + messageSubject + '\n' + messageBody
# Sending Email
server.sendmail(userEmail, recieverEmail, message)

server.quit()