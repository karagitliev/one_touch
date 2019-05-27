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
            'reg_time': time.time(),
        }
    }

    with open(cfg.USERS) as f:
        data = json.load(f)

    data.update(new_user)
    with open(cfg.USERS, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return True


def read_user_data(username, file):
    with open(file) as f:
        data = json.load(f)

    user_data = {
        'TOKEN': data[username]['1']['TOKEN'],
        'DEVICEID': data[username]['1']['DEVICEID'],
        'USERNAME': username,
        'PIN_ID': data[username]['1']['PIN_ID'],
    }

    return user_data


def write_user_data(username, user_data, file):
    with open(file) as f:
        data = json.load(f)

    if username in data:
        data[username].update(user_data)
    else:
        data[username] = user_data

    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return True
