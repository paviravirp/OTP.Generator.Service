
from sqlalchemy import *
from otp.config import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

db = create_engine(SQLALCHEMY_DATABASE_URI)
db.echo = False
dbmetadata = MetaData(db)
Base = declarative_base(metadata=dbmetadata)
Session = sessionmaker(bind = db)
session = Session()
