import smtplib

# smtpObj = smtplib.SMTP(host,port,local_hostname)

sender_mail = 'noreply@dfftech.com'

receivers_mail = ['saikiran.bavandla@gmail.com']

message = """ From: From Person %s

To: To Person %s

Subject: Sending SMTP e-mail

This is test e-mail message.

"""%(sender_mail, receivers_mail)


try:
    # smtpObj = smtplib.SMTP('localhost') 
    password = input('Enter the password')  
    smtpObj = smtplib.SMTP('zoho.com',465)  
    smtpObj.login(sender_mail,password)  
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
