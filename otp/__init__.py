from flask import Flask,jsonify,render_template
from otp.generator.views import generator
from otp.validator.views import validator
import os
import redis
from otp import config
from flask.ext.mail import Mail


app = Flask(__name__)
app.redis = redis.StrictRedis(host = 'localhost',port = 6379,db = 0)
app.register_blueprint(validator,url_prefix = '/validate/')
app.register_blueprint(generator,url_prefix = '/generate/')
mail = Mail(app)

@app.route('/ui/')
def ui():
	return render_template('generate.html')
app.config.from_object(config)
