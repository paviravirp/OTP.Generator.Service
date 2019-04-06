from datetime import datetime
from time import mktime
import time
from passlib.hash import sha256_crypt
import hashlib
from otp.models.Client import *

def current_datetime():
	return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

def get_string(value):
	return value.decode("utf-8")

def get_int(value):
	return (int.from_bytes(value,byteorder='little',signed = False) - 48)

def time_duration(time1, time2):
	return time1 - time2

def get_datetime(date_time):
	return datetime.fromtimestamp(mktime(time.strptime(date_time.decode("utf-8"),'%Y-%m-%d %H:%M:%S.%f')))

def encrypt(id):
	passwd = ""
	hash =sha256_crypt.encrypt(id)
	for letter in hash:
		passwd += str(ord(letter))
	passwd = passwd[:-9:-1]
	return passwd

def construct_request_id(id,param):
	request_object = hashlib.sha512((id.encode('utf-8')+(param.encode('utf-8'))))
	request_id = request_object.hexdigest()
	return (request_id)

def validate_client(token):
	client_id = Client.get_id(token)
	return client_id

