import logging
import onetouch_config as config


# FIXME move logger config to a dedicated file
def global_log(msg, session):
    logging.basicConfig(filename=config.GLOBAL_LOG, filemode='a', level=logging.DEBUG,
                        format=f'\n[{session}] %(asctime)s \n%(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.debug(f'{msg}')


def err_log(msg, session):
    logging.basicConfig(filename='logs/err_log.log', filemode='a',
                        format=f'[{session}] %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.error('This will get logged to a file')


def auth_log(msg, session):
    logging.basicConfig(filename=config.AUTH_LOG, filemode='a', level=logging.DEBUG,
                        format=f'\n[{session}] %(asctime)s \n%(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.debug(f'{msg}')
