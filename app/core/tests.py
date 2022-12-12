from config.wsgi import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string

from config import settings
from core.user.models import User


def send_email():
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado..')

        email_to = 'solanokevyn@gmail.com'
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        content = render_to_string('send_email.html', {'user': User.objects.get(pk=1)})
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

        print('Correo enviado correctamente')
    except Exception as e:
        print(e)


send_email()

"""
def __init__(self, server_url, upload_file_action, upload_msg_action, file, encoding, sendinterval, retryinterval):
      self.start_monitor_log()

def start_monitor_log(self):
		popen = subprocess.Popen('tail -f ' + self.fileurl, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		pid = popen.pid
		print "tail pid:", pid
		while True:
			line = popen.stdout.readline().strip()
			if line:
				self.msgqueue.put(line)
    
    
def __init__(self, server_url, upload_file_action, upload_msg_action, file, encoding, sendinterval, retryinterval):
		self.start_send_msg_task(self.sendinterval)

def start_send_msg_task(self, interval):
		try:
			logger.info("start msg sendding task, interval:" + bytes(interval))
			thread.start_new_thread(self.send_msg_task, ("msg_sending_thread", interval, ))
		except:
			logger.exception("start msg sending task failed")

def send_msg_task(self, threadName, interval):
		while True:
			list = []
			size = self.msgqueue.qsize()
			for i in range(0, size):
				list.append(base64.b64encode(self.msgqueue.get()))
			if len(list) > 0:
				msg = json.dumps(list)
				self.sendmsg(msg, self.MODE_NEW_MSG)
			time.sleep(interval)
"""