from datetime import datetime
from otp.models.OtpRequest import *
from otp.models.ClientTracking import *
from otp.models.Password import *
from otp.models.Client import *
from otp.config import *
from otp.utils import *
import otp
from celery_tasks.tasks import *


def otp_generate(client_id,param,ph_no):
	param = str(param)
	client = {}
	request_id = construct_request_id(client_id,param)
	request = {
		"requestId": request_id,
		"requestedAt": current_datetime(),
		"locked": False,
		"tries": 0,
		"param": param 
	}
	flag = 0
	otpreq = OtpRequest(client_id,param)
	otpreq.create()
	ct = ClientTracking.get_data(request_id)
	try:
		if ct:
			flag = 1
			tries = get_int(ct[b'tries'])
			tries += 1
			ct[b'tries'] = tries
			requestedAt = get_datetime(ct[b'requestedAt'])
			duration = datetime.utcnow() - requestedAt
			if ct[b'locked'].decode("utf-8") == "True":
				if duration.seconds >= MAXIMUM_REQUEST_INTERVAL:
					ClientTracking.unlock(request_id)
				else:
					raise Exception("Client locked")
			if tries >= MAXIMUM_RETRIES and duration.seconds <= MAXIMUM_REQUEST_INTERVAL :
				ClientTracking.setLock(request_id)
				raise Exception('Maximum tries exceeded')
			elif tries <= MAXIMUM_RETRIES and duration.seconds >= MAXIMUM_REQUEST_INTERVAL:
				ct[b'requestedAt'] = current_datetime()
				ct[b'tries'] = 0
				Password.delete(request_id)
		new_otp = Password(request_id)
		password = new_otp.create()
		Password.set_expire_time(request_id,PASSWORD_EXPIRY_TIME)
		if flag == 0:
			new_request = ClientTracking(request_id,request)
			new_request.insert()
		else:
			new_request = ClientTracking(request_id,ct)
			new_request.update()
		msg = "Password expires in "+str(PASSWORD_EXPIRY_TIME)+" seconds"
		mail_id = 'coolhot.pavi@gmail.com'
		send_sms.apply_async(args=(ph_no,password,msg,))
		send_email.apply_async(args=(mail_id,password,msg,))
		return "message sent"
	except Exception as e:
		return(e.args[0])
		
		


