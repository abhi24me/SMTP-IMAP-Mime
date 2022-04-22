# Importing required Libraries and Modules 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import emoji   #Just to use emoji 

#Below is a body of mail
mail_content ='''Hello,
This is a test mail.
In this mail I am sending an attachment of my python file.
The mail is sent using Python SMTP library.
Thank You.

Regards
Your_name
'''
#The mail addresses and password
sender_address = 'user_mail@gmail.com'
sender_pass = '************'
receiver_address = 'sender_mail@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Subject_Here'
#The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = "Attachment_Here"
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment

#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)

session.quit()
print('Mail Sent')


print(emoji.emojize("Mail Sent successfully :thumbs_up:")) #Just for fun
