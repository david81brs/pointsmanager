from flask_mongoengine import MongoEngine

db = MongoEngine()

def configure(APP):
    APP.config['SECRET_KEY'] = '123456790'
    APP.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
    db.init_app(APP)
    
    

