import smtplib

sender_email = "wick007john@gmail.com"
rec_email = "satyam2507mishra@gmail.com"
password = input(str("Please enter your password: "))
message = 

server = smtplib.SMTP('smptp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, rec_emailzz)