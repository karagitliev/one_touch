import os
from pyfiglet import figlet_format
from termcolor import colored


def main_menu(user_data):
    os.system('clear')

    header = figlet_format('MAIN MENU')
    header = colored(header, color='green')
    print(header)

    print(f'Please select an option                          Hello, {user_data["USERNAME"]}')
    print('-----------------------')

    print('1 - Buy dogfood')
    print('2 - Renew subscription')
    print('3 - Add new payment instrument')
    print('4 - View last 5 transactions')
    print('\n5 - Quit\n')

    usr_choice = input()


# main_menu()


def dogfood():
    pass


def renew_subscription():
    pass


def add_payment_instrument():
    pass


def payment_history():
    pass
