import redis
import os,json
from datetime import datetime
import otp
def insert_data(key,value):
	pip = otp.app.redis.pipeline()
	pip.hmset(key, value)
	pip.execute()

def update_data(key,value):
	otp.app.redis.delete(key)
	insert_data(key,value)
	
def get_value(key):
	return otp.app.redis.hgetall(key)

def get_expiry(key):
	return otp.app.redis.ttl(key)

def set_expiry(key,ttl):
	otp.app.redis.expire(key,ttl)

def delete_data(key):
	otp.app.redis.delete(key)
			