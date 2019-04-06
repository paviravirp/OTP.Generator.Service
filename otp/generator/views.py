from flask import Flask, jsonify,Blueprint,request,make_response
from otp.generator.services import *
from otp.utils import *

generator = Blueprint('generator',__name__)

@generator.route('/', methods=['POST'])
def generate():
	client_id = validate_client(request.headers.get('Authorization'))
	if client_id:
		message = otp_generate(client_id,request.json.get('param'), request.json.get('phone_no'))
	else:
		message = "Authorization failed"
	response = make_response(json.dumps(message))
	response.headers['Access-Control-Allow-Origin']='*'
	response.headers['Access-Control-Allow-Headers'] = 'Authorization'
	response.headers['Content-Type']="application/json"
	return response

