
from otp.celery_init import celery


def send_email(mail_id,password,msg):
	

	msg = Message("Hello",
                  sender="pavi.ravirp21@gmail.com",
                  recipients=["coolhot.pavi@gmail.com"])
	msg.body = "testing"
	msg.html = "<b>testing</b>"
	with otp.app.app_context():
		otp.mail.send(msg)