from datetime import datetime
import pytz,json
import traceback
from otp.config import *
from otp.utils import *
from otp.models.OtpValidate import *
from otp.models.ClientTracking import *
from otp.models.Password import *


def otp_validate(pwd,id,param):
		param = str(param)
		log = ""
		status = ""
		validateAt = current_datetime()
		flag = 0
		otp_List = {}
		request_id = construct_request_id(id,param)
		otp_List = Password.get_data(request_id)
		try:
			if not otp_List:
				log = "Time limit exceeded"
				status = 'failure'
				create_validate(id,param,status,log)
				raise Exception(log)
			else:
				retries = get_int(otp_List[b'retries'])
				retries += 1
				otp_List[b'retries'] = retries
				ttl = Password.get_expire_time(request_id)
				passwd = Password(request_id,otp_List)
				passwd.update()
				Password.set_expire_time(request_id,ttl)
				if retries >= MAXIMUM_RETRIES:
					ClientTracking.setLock(request_id)
					log = 'Maximum retries exceeded'
					status = 'failure'
					Password.delete(request_id)
					create_validate(id,param,status,log)
					raise Exception(log)
				if pwd == otp_List[b'password'].decode("utf-8"):
					flag = 1
					status = 'success'
					create_validate(id,param,status,log)
					Password.delete(request_id)
					ClientTracking.delete(request_id)
					return 'success'
				else:
					log = 'Password incorrect'
					status = 'failure'
					create_validate(id,param,status,log)
					return log
		except Exception as e:
			return(e.args[0])
			
			

def create_validate(id,param,status,log):
	otpval = OtpValidate(id,param,status,log)
	otpval.create()
