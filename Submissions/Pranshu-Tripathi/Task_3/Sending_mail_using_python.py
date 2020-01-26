import smtplib, ssl
mailid = input("Please enter Your email Id:\t")
password = input("Type your password and press enter:\t")
mailid_rec = input("Enter the mail id of receiver:\t")
message = input("Enter the message:\t")
server = smtplib.SMTP("smtp.gmail.com",587)
server.login(mailid,password)
server.sendmail(mailid,mailid_rec,message)