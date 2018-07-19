from app.views import configure as vwconfig
from flask import Flask, request, session
from flask_admin import Admin
from app.models.user import User, UserView, db
from flask_mongoengine import MongoEngine
from flask_babelex import Babel


BABEL = Babel()

@BABEL.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'pt_BR')


def create_app():

    APP = Flask(__name__)
    BABEL.init_app(APP)
    
    APP.config['SECRET_KEY'] = 'furfull-fellings'
    APP.config['MONGODB_SETTINGS'] = {'DB':'testing'}
    APP.config['FLASK_ADMIN_SWATCH']='slate'
    db.init_app(APP)
    vwconfig(APP)
    ADMIN = Admin(APP, name="Points Manager", template_mode="bootstrap3")
    ADMIN.add_view(UserView(User))
    return APP
