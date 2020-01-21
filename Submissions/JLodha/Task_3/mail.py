import smtplib,getpass
connection = smtplib.SMTP('smtp.gmail.com', 587)  
connection.starttls()
id = getpass.getpass('id:')
pwd = getpass.getpass('password: ')
connection.login(id, pwd)
rec = input("Enter the person whom you want to send the mail: ")
subject = input("Subject: ")
message = input('Message to Send: ')
finalmess = 'Subject: ' + subject+  "\n" + "Message: " + message
connection.sendmail(id,rec, finalmess)  
connection.quit() 