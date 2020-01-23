
import smtplib

content= 'HELLO WORLD'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('singhvishu26@gmail.com','******')
mail.sendmail('singhvishu26@gmail.com','iec2019019@iiita.ac.in',content)
mail.close()