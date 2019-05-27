from pprint import pprint

import onetouch_config as cfg
import onetouch_send_recv as send


def general_user_info(deviceid, token):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': deviceid,
        'TOKEN': token,
    }

    user_info = send.send_recv(cfg.USR_INF_GEN, params, 'USR INF GEN')
    return user_info


def pay_instruments_balance(pins):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': cfg.DEVICEID,
        'TOKEN': cfg.TOKEN,
        'PINS': pins,
    }

    pins_balance = send.send_recv(cfg.USR_INF_BALANCE, params, 'USR PINS BALANCE')
    return pins_balance


def pay_instruments(deviceid, token):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': deviceid,
        'TOKEN': token,
    }

    pins = send.send_recv(cfg.USR_INF_PINS, params, 'USR INF PINS')
    return pins['payment_instruments'][0]
