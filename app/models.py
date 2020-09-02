import mongoengine


class News(mongoengine.Document):
    title = mongoengine.StringField()
    author = mongoengine.StringField()
    content = mongoengine.StringField()
