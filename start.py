import onetouch_menu as menu
import random
import onetouch_menu as menu
import onetouch_logger as log
import onetouch_header as header
import onetouch_db_handler as db
import onetouch_authorisation as auth

SESSION = random.randint(10000, 99999)


def user_authenticate():
    header.header('LOGIN')

    while True:
        username = input('Please enter username: ')
        if username == '':
            continue
        else:
            break

    user_exists = db.check_user(username)
    if user_exists:
        log.global_log(f'User login success: {username}', SESSION)
    else:
        log.global_log(f'Create new user START: {username}', SESSION)
        auth.authorisation(username, SESSION)

    menu.main_menu(username)


user_authenticate()
