from .db_init import Base,session
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
from .redis_actions import *
from otp.config import *
from otp.utils import *
from sqlalchemy.dialects.postgresql import *

class OtpRequest(Base):
	__tablename__ = 'otpRequest'

	id = Column(Integer, primary_key=True)
	clientId = Column(String)
	requestedAt = Column(DateTime)
	param = Column(String)

	def __init__(self,clientId,param):
		self.clientId = clientId
		self.param = param
		self.requestedAt = datetime.utcnow()

	def create(self):
		session.add(self)
		session.commit()