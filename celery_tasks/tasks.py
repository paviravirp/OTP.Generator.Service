from otp.celery_init import celery
from twilio.rest import TwilioRestClient
from otp.config import *
from flask.ext.mail import Message
import otp

@celery.task(name='otp.msgsend')
def send_sms(ph_no,password,msg):
		client = TwilioRestClient(TWILIO_SID,TWILIO_AUTH_TOKEN)
		msg_to_send =  "Your one time password is "+password +". "+msg 
		msg_sent = client.messages.create(body=msg_to_send, from_ = TWILIO_PHONE_NUMBER, to=ph_no,)

@celery.task(name='otp.mailsend')
def send_email(mail_id,password,msg):
	mail = Message("One Time Password",
                  sender="pavi.ravirp21@gmail.com",
                  recipients=["coolhot.pavi@gmail.com"])
	mail.html = "Your one time password is "+password +". "+msg 
	with otp.app.app_context():
		otp.mail.send(mail)