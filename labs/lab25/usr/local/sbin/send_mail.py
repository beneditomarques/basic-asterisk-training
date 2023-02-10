#!/usr/bin/python3
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import os
from datetime import datetime


# Configs

smtp_server="smtp.mailosaur.net"
smtp_port=587
username = "wxdzvgfd@mailosaur.net"
sender_email = "wxdzvgfd@mailosaur.net"
password = "VwGdZU3PfwIhf1Bv"

# Functions

def format_count(count):
    
    if (len(str(count)) == 1):
        count = "000" + str(count)
    if (len(str(count)) == 2):
        count = "00" + str(count)
    if (len(str(count)) == 3):
        count = "0" + str(count)
    if (len(str(count)) == 4):
        count = count   
    return count



# Program

if (len(sys.argv) < 3):
    print("Insufficient arguments. Please use: sys.argv[0] extension_number audio_path")
    exit()

context = sys.argv[1]
extension_number = sys.argv[2]
count            = int(sys.argv[3]) - 1
formatted_count  = format_count(count)  
path_file        = '/var/spool/asterisk/voicemail/' + str(context) + '/' + str(extension_number) + '/INBOX/msg' + str(formatted_count)
filename         = path_file + '.WAV'



# Get message information from file

if os.path.isfile(path_file + '.txt'):
    mail_info = {}
    with open(path_file + '.txt') as f:
        content = f.readlines()
        content = content[4:]
        for line in content:
            (k, v) = line.split('=')
            mail_info[(k)] = v.replace('\n','')

# Build body

vm_dur      = mail_info['duration']
vm_date     = datetime.now().strftime("%c")
vm_callerid = mail_info['callerid'].replace("\"","")
vm_mailbox  = mail_info['origmailbox']
    
subject = "Asterisk - Correio de Voz: " + str(vm_mailbox)
body =  '<strong><font size=\'4\'>Nova mensagem correio de voz</font></strong>' \
        '<br>'\
        '<table align="left">'\
        '<tr><td><b>De:</b></td><td>'+str(vm_callerid)+'</td></tr>'\
        '<tr><td><b>Data:</b></td><td>'+str(vm_date)+'</td></tr>'\
        '<tr><td><b>Duração:</b></td><td>'+str(vm_dur)+'s</td></tr>'\
        '</table>'


# List destinations   
receivers = []
f = open("/etc/asterisk/voicemail_maillist.txt", "r")
for line in f.readlines():
    extension = line.split('=')[0].replace('\n','').replace(' ','')
    mail      = line.split('=')[1].replace('\n','').replace(' ','')
    if (extension == extension_number):
        receivers.append(mail)
f.close()

for receiver_email in receivers:
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "html"))


    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()    
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, text)

