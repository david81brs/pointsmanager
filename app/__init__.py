from app.views import configure as vwconfig
from app.db import db, configure as dbconfig
from flask import Flask
from flask_admin import Admin
from app.models.user import User, UserView

def create_app():
    APP = Flask(__name__)
    dbconfig(APP)
    vwconfig(APP)
    ADMIN = Admin(APP, name="Points Manager", template_mode="bootstrap3")
    ADMIN.add_view(UserView(User))
    return APP
