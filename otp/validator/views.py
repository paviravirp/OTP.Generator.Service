from flask import Flask,Blueprint,jsonify,request
from otp.validator.services import *
from otp.models.Client import *

validator = Blueprint('validator',__name__)


@validator.route('/', methods=['POST'])
def validate():
	client_id = validate_client(request.headers.get('Authorization'))
	if client_id:
		message = otp_validate(request.json.get('password'),client_id,request.json.get('param'))
	else: 
		message = "Authorization failed"
	return jsonify({'message': message})