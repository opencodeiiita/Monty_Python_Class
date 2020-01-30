import smtplib, getpass
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
id = getpass.getpass('mailid_sender:\t)
pwd = getpass.getpass('password:\t')
server.login(id,pwd)
reciever = input("Enter the mail ID of the reciever:\t")
subject = input("Sebject:\t")
message = input("message to convey:\t")
mail_body = "subject: " + subject + "\n" + "Message: " + message
server.sendmail(id,reciever,mail_body)
server.quit()

