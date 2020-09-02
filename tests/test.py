import requests
import json


def test_clear_base_for_tests():
    for i in json.loads(requests.get('http://localhost/get_news').text):
            requests.post('http://localhost/remove_news', data={'idnews': i['_id']['$oid']})
    assert len(json.loads(requests.get('http://localhost/get_news').text)) == 0


def test_status_api():
    assert requests.get('http://localhost/get_news').status_code == 200


def test_insert_api():
    for i in range(5):
        requests.post('http://localhost/insert_news', data={'title': str(i), 'author': str(i), 'content': str(i)})
    assert len(json.loads(requests.get('http://localhost/get_news').text)) == 5


def test_delete_api():
    for i in json.loads(requests.get('http://localhost/get_news').text):
        requests.post('http://localhost/remove_news', data={'idnews': i['_id']['$oid']})
    assert len(json.loads(requests.get('http://localhost/get_news').text)) == 0


def test_update_api():
    requests.post('http://localhost/insert_news', data={'title': 'title', 'author': 'author', 'content': 'author'})
    idnews= json.loads(requests.get('http://localhost/get_news').text)[0]['_id']['$oid']
    requests.post('http://localhost/update_news', data={'idnews':idnews, 'content':'content'})
    assert json.loads(requests.get('http://localhost/get_news').text)[0]['content'] == 'content'
