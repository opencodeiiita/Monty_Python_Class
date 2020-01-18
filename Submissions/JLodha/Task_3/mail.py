import smtplib 
connection = smtplib.SMTP('smtp.gmail.com', 587)  
connection.starttls()
connection.login("iit2019134@iiita.ac.in", "PASSWORDHERE")
message = "IIITian"
connection.sendmail("iit2019134@iiita.ac.in", "iit2019132@iiita.ac.in", message)  
connection.quit() 