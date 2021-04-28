from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

MY_ADDRESS = ""
PASSWORD = ""

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

host_string = "smtp-mail.outlook.com"
port_num = 587

s = smtplib.SMTP(host=host_string, port=port_num)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
names, emails = get_contacts('mycontacts.txt')
message_template = read_template('message.txt')

for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is a test program"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg