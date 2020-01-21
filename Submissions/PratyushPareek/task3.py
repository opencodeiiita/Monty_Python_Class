import smtplib

connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
connection.login('pareekpratyush2626@gmail.com','password')
connection.sendmail('pareekpratyush2626@gmail.com','iit2019184@iiita.ac.in','Subject: Life is meaningless \nNothing has a purpose\n')

