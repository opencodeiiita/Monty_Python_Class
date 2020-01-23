import smtplib 
gmailaddress = input("Your gmail address:  ")
gmailpassword = input("Password for that email address: ")
reciever = input("Receiver's email address: ")
subject=input("Enter subject of message")
msg = input("What is your message?  ")
FinalMail="Subject:"+subject+"\n"+"Message"+msg
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, reciever , msg)
print(" \n Sent!")
mailServer.quit()