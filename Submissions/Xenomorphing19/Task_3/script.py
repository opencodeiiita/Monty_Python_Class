import smtplib
import getpass
user=raw_input('Enter your email id:')
pwd= getpass.getpass("Enter Password[HIDDEN]")
print('enter the no. of reciepents')
x=int(input())
li = []
print('Enter the Reciepent\'s email id [PRESS ENTER AFTER EACH ID]')
for i in range(0,x):
    s=raw_input()
    li.insert(i,str(s))
print('Enter the message:')
mes=raw_input()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(str(user),str(pwd))
for i in range(len(li)):  
    message =str(mes)
    s.sendmail(str(user),l[i],message) 
s.quit() 
