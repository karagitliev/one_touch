import os
from termcolor import colored
from pyfiglet import figlet_format


def header(title, username='Guest'):
    os.system('clear')

    header = figlet_format(title)
    header = colored(header, color='green')
    print(header)
    print(f'                                         Hello, {username}')
    print('-----------------------------------------------------\n')
