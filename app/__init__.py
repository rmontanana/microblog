from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Puestos fuera del tutorial
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# sets de default login view
login.login_view = "login"

from app import routes, models
