import os
import random
from pyfiglet import figlet_format
from termcolor import colored

import onetouch_logger as log
import onetouch_db_handler as db
import onetouch_authorisation as auth_start

SESSION = random.randint(10000, 99999)


def user_authenticate():
    os.system('clear')

    header = figlet_format('LOGIN')
    header = colored(header, color='green')
    print(header)

    while True:
        username = str(input('Please enter username: '))
        if username == '':
            continue
        else:
            break

    user_exists = db.check_user(username)

    if user_exists is True:
        print('Please choose an option from the menu')
    else:
        create_new_user = db.create_user(username)
        if create_new_user is True:
            log.global_log(f'Create new user START: {username}', SESSION)
            auth_start.authorisation()


user_authenticate()
