from celery import Celery
from flask import Flask

celery = Celery('otp')
celery.config_from_object('otp.config')