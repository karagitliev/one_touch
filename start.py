import os
import random
from pyfiglet import figlet_format
from termcolor import colored

import menu
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

    user_data = db.check_user(username)

    if user_data:
        log.global_log(f'User login success: {username}', SESSION)
        menu.main_menu(user_data)
    else:
        log.global_log(f'Create new user START: {username}', SESSION)
        create_new_user = auth_start.authorisation(username, SESSION)

    if create_new_user is True:
        db.create_user(username)


user_authenticate()
