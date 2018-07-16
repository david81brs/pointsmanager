from flask_mongoengine import MongoEngine
from flask_admin.contrib.mongoengine import ModelView

db = MongoEngine()

class User(db.Document):
    name = db.StringField(max_length=100)

    def __unicode__(self):
        return self.name

class UserView(ModelView):
    column_filters = ['name']
