from app.db import db
from flask_admin.contrib.mongoengine import ModelView

class User(db.Document):
    name = db.StringField(max_length=100)

    def __unicode__(self):
        return self.name

class UserView(ModelView):
    column_filters = ['name']