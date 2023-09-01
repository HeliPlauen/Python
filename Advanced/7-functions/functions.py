import statistics
import datetime
import smtplib
from email.mime.text import MIMEText


def arythmetic_mean(some_list:list):
    if len(some_list):
        return statistics.mean(some_list)
    else:
        raise ValueError


def delet_val_from_list(some_list:list, value):
    while value in some_list:
        some_list.remove(value)
    return some_list


# Useless function!!!!
def create_user(first_name:str, last_name:str, born:datetime.date, address:str):
    message = "Testing Unittest!!! New user registered!!!"
    send_email(address, message)


def send_email(address, message):

    # Pinnt information
    print(address)
    print(message)

    # Set the SMTP server and login credentials
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "for.work.miraplay@gmail.com"
    password = "shjchojlgeqlunba"

    # Set the email parameters
    fromaddr = "for.work.miraplay@gmail.com"
    toaddr = address
    subject = "Registration"
    body = message

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



