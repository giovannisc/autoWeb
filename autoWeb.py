import os, multiprocessing, logging, platform
from flask_sqlalchemy import SQLAlchemy

from App import initApp
from config import Config

log = logging.getLogger('werkzeug')
log.disabled = not Config.DEBUG

app = initApp()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASEURL
db = SQLAlchemy(app)

if __name__ == '__main__':
	if platform.system() == "Windows":
		# On Windows calling this function is necessary.
		multiprocessing.freeze_support()
	app.run(host="0.0.0.0", port=8000, debug = Config.DEBUG)