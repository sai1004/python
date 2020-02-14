import smtplib
# Calling SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)
# TLS for network security
s.starttls()
# User email Authentication
s.login("sender_email_id", "sender_email_id_password")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)
