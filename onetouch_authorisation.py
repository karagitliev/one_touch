import random
import webbrowser
import urllib.parse

import onetouch_config as cfg
import onetouch_send_recv as send
import onetouch_user_info as user_info
import onetouch_db_handler as db


def authorisation(username, SESSION):
    key = random.randint(10000000, 99999999)
    deviceid = username + '_' + str(random.randint(1000000000, 9999999999))

    params = {
        'APPID': cfg.APPID,
        'DEVICEID': deviceid,
        'KEY': key,
    }

    # This opens a browser and loads ePay.bg for user authorisation
    req_string = urllib.parse.urlencode(params)
    webbrowser.open_new(cfg.AUTH_START + req_string)

    # Get code
    req_code = send.send_recv(cfg.AUTH_VERIFY, params, 'GET CODE')
    params['CODE'] = req_code['code']

    # Actual TOKEN receipt
    req_token = send.send_recv(cfg.AUTH_GET_TOKEN, params, 'AUTHORISATION')

    # Get user payment instruments
    # Should add logic for more than 1 payment instrument #FIXME
    pins = user_info.pay_instruments(deviceid, req_token['TOKEN'])
    params = {
        '1': {
            'KEY': key,
            'NAME': pins['NAME'],
            'CODE': params['CODE'],
            'TOKEN': req_token['TOKEN'],
            'PIN_ID': pins['ID'],
            'EXPIRES': pins['EXPIRES'],
            'PIN_TYPE': pins['TYPE'],
            'DEVICEID': deviceid,
        }
    }
    db.write_user_data(username, params, cfg.USERS_PINS)
    db.create_user(username)
    # check if db record is success #FIXME

    req_user_info = user_info.general_user_info(deviceid, req_token['TOKEN'])
    params = {
        'KIN': req_user_info['userinfo']['KIN'],
        'GSM': req_user_info['userinfo']['GSM'],
        'EMAIL': req_user_info['userinfo']['EMAIL'],
        'REAL_NAME': req_user_info['userinfo']['REAL_NAME'],
    }
    db.write_user_data(username, params, cfg.USERS_DATA)
