import datetime as dt
import time
import smtplib
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('toantran11.gl@gmail.com', 'Toantretrau0211')
    message = 'sending this from python!'
    server.sendmail('toantran11.gl@gmail.com', 'toantran12.gl@gmail.com ', message)
    server.quit()
send_email()