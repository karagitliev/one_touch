import json
import time
import onetouch_config as cfg


def check_user(username):
    user_exists = False
    with open(cfg.USERS) as json_file:
        data = json.load(json_file)
        if username in data:
            user_exists = True
            return(user_exists)
        else:
            new_user = create_user(username)

    return(user_exists)


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
