# Example script to send an email

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("naveen.sathyatech@gmail.com","django3128")
server.sendmail("naveen.sathyatech@gmail.com","naveenzoom6@gmail.com","This is a test mail by Python Developers")

print("Mail Sent")


