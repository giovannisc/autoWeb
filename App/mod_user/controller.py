from flask_restplus import Namespace, Resource
from flask import render_template
login = Namespace("login",
        description ='Login Operations')

@login.route('/')
class Login(Resource):
	def get(self):
		return "nothing to do", 200
	def post(self):
		
		return "foi", 200