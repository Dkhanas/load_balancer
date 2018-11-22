import json


def get_servers_data():
    with open('servers_list.json', 'r') as f:
        data = f.read()
    return json.loads(data) if data else []


def set_servers_data(data, port):
    with open('servers_list.json', 'w') as f:
        if port not in data:
            data.append(port)
        f.write(json.dumps(data))


def delete_server(key):
    data = get_servers_data()
    data.remove(key)
    with open('servers_list.json', 'w') as f:
        f.write(json.dumps(data))
