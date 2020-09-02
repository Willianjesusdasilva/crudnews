from mongoengine import connect
from models import News
from bson import ObjectId
import json


class odm_news:

    def __init__(self):
        self.Connect = connect('newsblog', host='host.docker.internal', port=27017)

    def get_news(self, filter_news):
        return News.objects.filter(**filter_news).to_json()

    def insert_news(self, news_json):
        News.from_json(json.dumps(news_json, sort_keys=True)).save()

    def remove_news(self, id_news):
        News.objects(id=ObjectId(id_news)).delete()

    def update_news(self, news_json):
        id_news = news_json.pop('idnews')
        News.objects(id=ObjectId(id_news)).update(**news_json)
