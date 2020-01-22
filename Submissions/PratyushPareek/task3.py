import smtplib

senderEmailID = input()
password = input()
recieverEmailID = input()
Subject = input()
Body = input()

connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
connection.login(senderEmailID,password)
connection.sendmail(senderEmailID,recieverEmailID,'Subject: '+Subject+ '\n' + Body)

