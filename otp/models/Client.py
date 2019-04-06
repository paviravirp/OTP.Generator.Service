from .db_init import Base,session
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import *

class Client(Base):
	__tablename__ = 'client'

	clientId = Column(String, primary_key=True)
	token = Column(String)

	@classmethod
	def get_id(self,token):
		client_id = session.query(self.clientId).filter(self.token == token).first()
		return str(client_id)