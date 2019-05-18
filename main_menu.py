import os
from pyfiglet import figlet_format
from termcolor import colored
import onetouch_db_handler as db


def start():
    os.system('clear')

    header = figlet_format('MAIN MENU')
    header = colored(header, 'red')
    print(header)


start()
