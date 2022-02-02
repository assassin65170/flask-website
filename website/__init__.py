from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oagxhhbpuziukq:428a2b42a3b4be7211a9bb982ce94a4eb933efa2cce80926d3068c54c4f1f9d0@ec2-3-230-199-240.compute-1.amazonaws.com:5432/d8u82f615vf2ii'
app.config["SECRET_KEY"] = "0x111f526fosMs36geNrYr35wQMr"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from website import routes
