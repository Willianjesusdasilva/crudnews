from flask import Flask, request
from odm import odm_news
import json


app = Flask(__name__)


@app.route('/get_news', methods=["GET"])
def get_news_route():
    Odm_news = odm_news()
    return Odm_news.get_news(request.form.to_dict())


@app.route('/insert_news', methods=["POST"])
def insert_news_route():
    Odm_news = odm_news()
    Odm_news.insert_news(request.form.to_dict())
    return json.dumps({'validation': 'True'}, sort_keys=True)


@app.route('/remove_news', methods=["POST"])
def remove_news_route():
    Odm_news = odm_news()
    Odm_news.remove_news(request.form['idnews'])
    return json.dumps({'validation': 'True'}, sort_keys=True)


@app.route('/update_news', methods=["POST"])
def update_news_route():
    Odm_news = odm_news()
    Odm_news.update_news(request.form.to_dict())
    return json.dumps({'validation': 'True'}, sort_keys=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
