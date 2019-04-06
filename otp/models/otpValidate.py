from .db_init import Base,session
from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
from .redis_actions import *
from otp.config import *
from otp.utils import *
from sqlalchemy.dialects.postgresql import *

class OtpValidate(Base):
	__tablename__ = 'otpValidate'

	id = Column(Integer, primary_key=True)
	clientId = Column(String)
	validatedAt = Column(DateTime)
	param = Column(String)
	status = Column(String)
	resultLog = Column(String)

	def __init__(self,clientId,param,status,log):
		self.clientId = clientId
		self.param = param
		self.status = status
		self.resultLog = log
		self.validatedAt = datetime.utcnow()

	def create(self):
		session.add(self)
		session.commit()