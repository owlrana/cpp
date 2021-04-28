from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

<<<<<<< HEAD
MY_ADDRESS = "keepitahundred@outlook.com"
PASSWORD = "#PODCAST@indian"
=======
sender_email = "rahulrana@null.net"
rec_email = "satyam2507mishra@gmail.com"
password = input(str("Please enter your password: "))
message = "Hey! This is my first email sent via python!"
>>>>>>> d2ec7a983a9c9a0bf1b007246a434b1776ee9e90

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

if 'outlook' in MY_ADDRESS:
    host_string = "smtp-mail.outlook.com"
    port_num = 587
elif 'gmail' in MY_ADDRESS:
    host_string = "imap.gmail.com"
    port_num = 993

s = smtplib.SMTP(host=host_string, port=port_num)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
message_template = read_template('message.txt')
names, emails = get_contacts('mycontacts.txt')


for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is a test program"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg