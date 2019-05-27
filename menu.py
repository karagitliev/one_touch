from sys import exit
from time import sleep
from termcolor import colored
from pyfiglet import figlet_format

import os
import onetouch_config as cfg
import onetouch_payment as payment
import onetouch_db_handler as db


def header(title, username):
    os.system('clear')

    header = figlet_format(title)
    header = colored(header, color='green')
    print(header)
    print(f'                                         Hello, {username}')
    print('-----------------------------------------------------\n')


def main_menu(username):
    header('MAIN MENU', username)

    print('1 - Buy dogfood')
    print('2 - Renew subscription')
    print('3 - Add new payment instrument')
    print('4 - View last 5 transactions')
    print('\n5 - Quit\n')

    user_data = db.read_user_data(username, cfg.USERS_PINS)

    usr_choice = input('Please choose an option: ')
    if usr_choice == '1':
        dogfood(username, user_data)
    elif usr_choice == '2':
        renew_subscription()
    elif usr_choice == '3':
        add_payment_instrument()
    elif usr_choice == '4':
        payment_history()
    elif usr_choice == '5':
        exit()


def dogfood(username, user_data):
    food = None
    amount = 0
    usr_choice = None
    while usr_choice != '4':
        header('DOG FOOD', username)
        print('1 - Chicken - 12.99')
        print('2 - Beef - 15.99')
        print('3 - Premium Pork with apples - 20.99')
        print('\n4 - Back to main menu')

        usr_choice = input('\nPlease choose an option: ')
        if usr_choice == '1':
            amount = 12.99
            food = 'Chicken'
        elif usr_choice == '2':
            amount = 15.99
            food = 'Beef'
        elif usr_choice == '3':
            amount = 20.99
            food = 'Premium Pork with apples'
        elif usr_choice == '4':
            main_menu(username)

        (tax, total, params) = payment.get_taxes(username, amount, user_data)
        print(f'\n----------------\n{food}')
        print(f'\nAmount: {amount}\nBank tax: {tax / 100}')
        print(f'Total: {(total / 100):.2f}\n\nConfirm purchase? y/n')

        usr_choice = input().upper()
        if usr_choice == 'Y':
            payment.payment(username, params)  # FIXME check status here
            print('Payment successful')
            print('\n1 - Make another purchase')
            print('2 - Back to Main menu')

            usr_choice = input().upper()
            if usr_choice == '1':
                dogfood(username, user_data)
            else:
                main_menu(username)
        else:
            print('\nTransaction cancelled, returning to Main menu')
            sleep(3)
            dogfood(username, user_data)


def renew_subscription():
    pass


def add_payment_instrument():
    pass


def payment_history():
    pass
