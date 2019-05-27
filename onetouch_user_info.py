from pprint import pprint

import onetouch_config as cfg
import onetouch_send_recv as req


def general_user_info(deviceid, token):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': deviceid,
        'TOKEN': token,
    }
    url = cfg.USR_INF_GEN
    req_type = 'usr_inf_gen'
    user_info = req.send_recv(url, params, req_type)

    return user_info


def pay_instruments_balance(pins):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': cfg.DEVICEID,
        'TOKEN': cfg.TOKEN,
        'PINS': pins,
    }
    url = cfg.USR_INF_BALANCE
    req_type = 'usr_inf_balance'
    pins_balance = req.send_recv(url, params, req_type)

    print('\n### User payment instruments balance ###')
    pprint(pins_balance)


def pay_instruments(deviceid, token):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': deviceid,
        'TOKEN': token,
    }
    url = cfg.USR_INF_PINS
    req_type = 'usr_inf_pins'
    pins = req.send_recv(url, params, req_type)

    return pins['payment_instruments'][0]
