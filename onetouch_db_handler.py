import json
import time
import onetouch_config as cfg


def check_user(username):
    with open(cfg.USERS) as json_file:
        data = json.load(json_file)
        if username in data:
            return True


def create_user(username):
    new_user = {
        username: {
            'active': 1,
            'reg_time': int(time.time()),
        }
    }

    with open(cfg.USERS) as f:
        data = json.load(f)

    data.update(new_user)
    with open(cfg.USERS, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return True


def read_user_data(username):
    with open(cfg.USER_DATA) as f:
        data = json.load(f)

    user_data = {
        'TOKEN': data[username]['TOKEN'],
        'DEVICEID': data[username]['DEVICEID'],
        'USERNAME': username,
    }

    return user_data


def write_user_data(username, user_data, file):
    with open(file) as f:
        data = json.load(f)

    data.update(user_data)
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return True
