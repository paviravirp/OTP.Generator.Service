## Setup
---

Steps to get your development environment for this project. 

* Install Python 3

		[Pyhon](https://www.python.org/downloads/)

* Install tools and other dependencies

        	[PostgreSQL](http://www.postgresql.org/)
        	[redis](http://redis.io/)

* Source Repository

        	Fork otp-generation in git.
    		Clone the repo to the dev machine.

        		cd ~/git|/desired/path
                git clone https://github.com/<git-login-name>/OTP.Generator.Service.git

* OTP project

        	Clone the repo
        	cd to repo
        	pip3 install virtualenv
        	virtualenv venv
        	source venv/Scripts/activate
        	pip3 install -r requirements.txt
        	create database ‘OTP_Generation’ with user ‘postgres’
        	Create table 'otprequest' with fields clientid(text),requestedat(timestamp),param(text)
        	Create table 'otpvalidate' with fields clientid(text), validatedat(timestamp),status(text), result(text)
        	start Redis server
        	python manager.py
        	To update the requirements.txt
            	pip freeze > requirements.txt
        	Hit localhost:5000/generate/<context> to generate password
        	Hit localhost:5000/validate/<context> to validate password

			Example for context:
			 	login
				registeration
				payment
				forgot_password
        

    