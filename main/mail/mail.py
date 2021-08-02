import smtplib, ssl
import logging as log
import main.share as share
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from util.file_util import read_template
from main.timez import TimeZ
from main.crypto.crypto import Crypto

#-------------
# Mail class
#-------------
class Mail(TimeZ):

  def __init__(self):
    self.crypto = Crypto()

  def send(self, attendance):
    log.debug('Send email')
    # Prepare data for email
    check_in = self.convert_tz(attendance['check_in'])
    check_out = self.convert_tz(attendance['check_out'])
    # Prepare template data
    template_data = {
      'WORKING_DAY': check_in.date().strftime('%d-%m-%Y'),
      'CHECK_IN_TIME': check_in.time(),
      'CHECK_OUT_TIME': check_out.time()
    }
    # Get template name
    template_name = 'check-in'
    if check_in != check_out:
      template_name = 'check-out'
    # Read template
    message_template = read_template(template_name)

    smtp_server = share.config['mail']['smtp-server']
    port = share.config['mail']['port']
    sender_email = share.config['mail']['sender-email']
    sender_name = share.config['mail']['sender-name']
    password = self.crypto.decrypt(share.config['mail']['password'])
    receiver_email = share.config['mail']['receiver-email']

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Create message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'CHECKIN' if template_name == 'check-in' else 'CHECKOUT'
    message['From'] = f'{sender_name} <{sender_email}>'
    message['To'] = receiver_email
    html = message_template.substitute(template_data)

    # part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
