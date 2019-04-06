
from .db_init import Base,session
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
from .redis_actions import *
from otp.config import *
from otp.utils import *
from sqlalchemy.dialects.postgresql import *


class Password(object):

	id = Column(String)
	data = Column(HSTORE)

	def __init__(self,id,data=None):
		pwd_prefix = "PWD::"
		pwd_id = pwd_prefix + str(id)
		self.id = pwd_id
		self.data = data

	def create(self):
		self.data = self.generate_password(self.id)
		insert_data(self.id,self.data)
		return self.data["password"]

	def delete(id):
		pwd_prefix = "PWD::"
		pwd_id = pwd_prefix + str(id)
		delete_data(pwd_id)

	def update(self):
		update_data(self.id,self.data)

	@classmethod
	def generate_password(self,id):
		pwd = {}
		pwd["clientId"] = id
		pwd["password"] = encrypt(id)
		pwd["retries"] = 0
		return pwd

	@classmethod
	def get_data(self,id):
		pwd_prefix = "PWD::"
		pwd_id = pwd_prefix + str(id)
		return get_value(pwd_id)

	@classmethod
	def get_expire_time(self,id):
		pwd_prefix = "PWD::"
		pwd_id = pwd_prefix + str(id)
		return get_expiry(pwd_id)

	@classmethod
	def set_expire_time(self,id,ttl):
		pwd_prefix = "PWD::"
		pwd_id = pwd_prefix + str(id)
		return set_expiry(pwd_id,ttl)	