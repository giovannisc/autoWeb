from flask import Flask
from flask_restplus import Api
from flask_login import LoginManager
from flask_cors import CORS
import os

from config import Config

login_manager = LoginManager()

def initApp():
	#initializations 
	app = Flask(__name__, instance_relative_config=True, template_folder=".")
	app.secret_key = os.urandom(16)
	login_manager.init_app(app)
	CORS(app)
	api = Api(app, version=Config.VERSION, title=Config.NAME,
				description=Config.DESCRIPTION,
			)
	from .mod_user.controller import login
	api.add_namespace(login)
	return app