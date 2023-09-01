import smtplib


fromaddr = "for.work.miraplay@gmail.com"  
toaddrs  = "oleg.shcherbatiouk@gmail.com"  
msg = "This is a test email sent from Python." 
      
username = "for.work.miraplay@gmail.com"
password = "shjchojlgeqlunba"

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
#server.ehlo()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()