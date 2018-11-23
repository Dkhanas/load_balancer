import requests

from flask import Flask
from requests import ConnectionError

from utils import delete_server, get_servers_data

app = Flask(__name__)

SERVER_COUNTER = 0
IP = '127.0.0.1'


def check_data():
    global SERVER_COUNTER
    global PORTS

    data = get_servers_data()
    PORTS = data
    if SERVER_COUNTER == len(data):
        SERVER_COUNTER = 0


def get_next_server():
    global SERVER_COUNTER

    try:
        response = requests.get(url=u'http://{}:{}'.format(IP, PORTS[SERVER_COUNTER]))
        if response.status_code < 400:
            return 'Response server {}:{} at {}'.format(IP, PORTS[SERVER_COUNTER], response.text)
        else:
            return clean_servers()
    except ConnectionError:
        return clean_servers()

    except IndexError:
        return 'No available services'


def clean_servers():
    delete_server(PORTS[SERVER_COUNTER])
    check_data()
    return get_next_server()


@app.before_request
def before_index_request():
    check_data()


@app.after_request
def after_index_request(response):
    global SERVER_COUNTER
    SERVER_COUNTER += 1
    return response


@app.route("/")
def index():
    response = get_next_server()
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
