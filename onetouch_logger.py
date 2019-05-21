import logging
session = 12


def log(msg, type, session):
    if type == 'global':
        pass
    elif type == 'err':
        pass
    elif type == 'timeout':
        pass


# FIXME move logger config to a dedicated file
def global_log(msg, type, session):
    logging.basicConfig(filename='logs/global_log.log', filemode='a',
                        format=f'[{session}] %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.debug('This will get logged to a file')


def err_log(msg, type, session):
    logging.basicConfig(filename='logs/err_log.log', filemode='a',
                        format=f'[{session}] %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.error('This will get logged to a file')


def timeout_log(msg, type, session):
    logging.basicConfig(filename='logs/timeout_log.log', filemode='a',
                        format=f'[{session}] %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    logging.info('This will get logged to a file')
