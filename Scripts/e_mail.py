import smtplib
from email.mime.text import MIMEText


# Set the SMTP server and login credentials
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "for.work.miraplay@gmail.com"
password = "shjchojlgeqlunba"

# Set the email parameters
fromaddr = "for.work.miraplay@gmail.com"
toaddr = "oleg.shcherbatiouk@gmail.com"
subject = "Test email from Python"
body = "This is a test email sent from Python."

# Create the email message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = fromaddr
msg["To"] = toaddr

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()