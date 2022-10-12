from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
import sqlalchemy
from config import Config
from flask_login import LoginManager

# intializing
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
login = LoginManager(app)

login.login_view = 'login'
login.login_message = 'Log in please'
login.login_message_category = 'warning'



from app import routes, models
