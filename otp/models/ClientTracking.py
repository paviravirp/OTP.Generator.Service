
from .db_init import Base,session
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
from .redis_actions import *
from otp.config import *
from otp.utils import *
from sqlalchemy.dialects.postgresql import *


class ClientTracking(object):
	
	id = Column(String)
	data = Column(HSTORE)

	def __init__(self,id,data):
		request_prefix = "CLIENT::"
		request_id = request_prefix + str(id)
		self.id = request_id
		self.data = data

	def insert(self):
		insert_data(self.id,self.data)

	def update(self):
		update_data(self.id,self.data)

	def delete(id):
		request_prefix = "CLIENT::"
		request_id = request_prefix + str(id)
		delete_data(request_id)

	@classmethod
	def setLock(self,id):
		request_prefix = "CLIENT::"
		request_id = request_prefix + str(id)
		ct = get_value(request_id)
		ct[b'locked'] = True
		ct[b'requestedAt'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
		ct[b'tries'] = MAXIMUM_RETRIES
		update_data(request_id,ct)

	@classmethod
	def unlock(self,id):
		request_prefix = "CLIENT::"
		request_id = request_prefix + str(id)
		ct = get_value(request_id)
		ct[b'locked'] = False
		ct[b'requestedAt'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
		ct[b'tries'] = 0
		update_data(request_id,ct)
	
	@classmethod
	def get_data(self,id):
		request_prefix = "CLIENT::"
		request_id = request_prefix + str(id)
		return get_value(request_id)