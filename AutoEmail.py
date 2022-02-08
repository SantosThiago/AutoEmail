import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#reading file with emails
with open("emails.txt","r") as file:
    emailFile=file.readlines()

#adding emails to a list
emailList=[]
for email in emailFile:
    email=email.replace('\n',"")
    emailList.append(email)
print(emailList)

# setuping
host = "smtp.gmail.com" #example host mail
port = 587
user = "email"
password = "password"

# Creating object
print('Creating server object...')
server = smtplib.SMTP(host, port)

# Login with server
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Creating message
message = 'Hello World'
print('Creating message...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['Subject'] = "Testing AutoEMail"
print('Adding text...')
email_msg.attach(MIMEText(message, 'plain'))

# Sending message
print('Sending message...')
for email in emailList:
    server.sendmail(email_msg['From'], email, email_msg.as_string())
print('Mensage sent!')
server.quit()
