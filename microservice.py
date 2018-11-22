import datetime
import json

from flask import Flask

from utils import get_servers_data, set_servers_data

app = Flask(__name__)


@app.route("/")
def index():
    return json.dumps({
        'data_time': datetime.datetime.now().strftime('%Y %m %d %X')
    })


if __name__ == '__main__':
    import sys
    args = sys.argv
    port = sys.argv[1]
    data = get_servers_data()
    set_servers_data(data, port)
    app.run(host='127.0.0.1', port=port)
