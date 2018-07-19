from app.views import configure as vwconfig
from flask import Flask
from flask_admin import Admin
from app.models.user import User, UserView, db
from flask_mongoengine import MongoEngine

def create_app():
    APP = Flask(__name__)
    APP.config['SECRET_KEY'] = 'furfull-fellings'
    APP.config['MONGODB_SETTINGS'] = {'DB':'testing'}
    APP.config['FLASK_ADMIN_SWATCH']='slate'
    db.init_app(APP)
    vwconfig(APP)
    ADMIN = Admin(APP, name="Points Manager", template_mode="bootstrap3")
    ADMIN.add_view(UserView(User))
    return APP
