import os
from sys import exit
from pyfiglet import figlet_format
from termcolor import colored
import onetouch_config as cfg
import onetouch_payment as payment
import onetouch_db_handler as db


def main_menu(username):
    os.system('clear')

    header = figlet_format('MAIN MENU')
    header = colored(header, color='green')
    print(header)

    print(f'Please select an option                          Hello, {username}')
    print('-----------------------')

    print('1 - Buy dogfood')
    print('2 - Renew subscription')
    print('3 - Add new payment instrument')
    print('4 - View last 5 transactions')
    print('\n5 - Quit\n')

    user_data = db.read_user_data(username, cfg.USERS_PINS)
    print(user_data)

    usr_choice = input()
    if usr_choice == '1':
        resp = dogfood(username, user_data)
    elif usr_choice == '2':
        resp = renew_subscription()
    elif usr_choice == '3':
        resp = add_payment_instrument()
    elif usr_choice == '4':
        resp = payment_history()
    elif usr_choice == '5':
        exit()

    print(resp)


# main_menu()


def dogfood(username, user_data):
    resp = payment.payment(username, user_data)
    return 'Payment success'


def renew_subscription():
    pass


def add_payment_instrument():
    pass


def payment_history():
    pass
