import requests

HOST = 'http://127.0.0.1'
PORT = '5000'


def get_url(host=HOST, port=PORT):
    return '{}:{}'.format(host, port)


def test_server_available():
    response = requests.get(get_url())
    assert response.status_code == 200


def test_empty_microservises():
    response = requests.get(get_url())
    assert response.text == 'No available services'

