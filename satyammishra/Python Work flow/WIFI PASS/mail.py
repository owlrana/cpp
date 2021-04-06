import smtplib

sender_email = "rahulrana@null.net"
rec_email = "satyam2507mishra@gmail.com"
password = input(str("Please enter your password: "))
message = "Hey! This is my first email sent via python!"

server = smtplib.SMTP('smptp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, rec_email, message)