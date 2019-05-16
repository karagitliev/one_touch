import random
from pprint import pprint

import onetouch_config as config
import onetouch_urls as urls
import onetouch_send_recv as req

SESSION = random.randint(10000, 99999)


def general_user_info():
    params = {
        'APPID': config.APPID,
        'DEVICEID': config.DEVICEID,
        'TOKEN': config.TOKEN,
    }
    url = urls.USR_INF_GEN
    req_type = 'usr_inf_gen'
    user_info = req.send_recv(url, params, req_type)

    print('\n### General user info ###')
    pprint(user_info['userinfo'])


general_user_info()


def pay_instruments_balance(pins):
    params = {
        'APPID': config.APPID,
        'DEVICEID': config.DEVICEID,
        'TOKEN': config.TOKEN,
        'PINS': pins,
    }
    url = urls.USR_INF_BALANCE
    req_type = 'usr_inf_balance'
    pins_balance = req.send_recv(url, params, req_type)

    print('\n### User payment instruments balance ###')
    pprint(pins_balance)


def pay_instruments():
    params = {
        'APPID': config.APPID,
        'DEVICEID': config.DEVICEID,
        'TOKEN': config.TOKEN,
    }
    url = urls.USR_INF_PINS
    req_type = 'usr_inf_pins'
    pins = req.send_recv(url, params, req_type)

    print('\n### User payment instruments info ###')
    pprint(pins)

    pins = pins['payment_instruments'][0]['ID']
    pins_balance = pay_instruments_balance(pins)


pay_instruments()
