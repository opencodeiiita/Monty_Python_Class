
import smtplib

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender_id=input("Enter your email-id:")
sender_pswd=input("Enter your pswd:")
reciever_id=input("Enter reciever's email handle:")
content=input("Enter the body of email: ")
mail.login(sender_id,sender_pswd)
mail.sendmail(sender_id,reciever_id,content)
mail.close()