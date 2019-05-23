import random
import requests
import webbrowser
import urllib.parse
from sys import exit
from time import sleep

import onetouch_user_info as usr_inf
import onetouch_config as cfg
import onetouch_db_handler as db


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    if req.status_code == requests.codes.ok:
        req_json = req.json()
        if req_json['status'] == 'OK':
            return req_json
        else:
            failcount = 0
            while req_json['status'] != 'OK':
                sleep(3)
                failcount += 3
                req = requests.get(url + query_string)
                req_json = req.json()
                if failcount > cfg.AUTH_TIMEOUT:
                    exit(f'{req_type} TIMEOUT')
            if req_json['status'] == 'OK':
                return req_json
            else:
                exit(f'{req_type} TIMEOUT')
    # add else in case of http status != 200 #FIXME


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
#    log.auth_log(f'USER REDIRECTED TO EPAY: {username}', SESSION)

    # Get code
    req_type = 'GET CODE'
    resp = send_recv(cfg.AUTH_VERIFY, params, req_type)
    params['CODE'] = resp['code']
#    log.auth_log(f'GET CODE SUCCESS: {resp}', SESSION)

    # Actual TOKEN receipt
    req_type = 'AUTHORISATION'
    resp = send_recv(cfg.AUTH_GET_TOKEN, params, req_type)
#    log.auth_log(f'GET TOKEN SUCCESS: {resp}', SESSION)

    # Get user payment instruments
    pins = usr_inf.pay_instruments(deviceid, resp['TOKEN'])
    # Should add logic for more than 1 payment instrument #FIXME

    user_data = {
        username: {
            'KEY': key,
            'CODE': params['CODE'],
            'TOKEN': resp['TOKEN'],
            'DEVICEID': deviceid,
            'pins': {
                pins['NAME']: {
                    'PIN_ID': pins['ID'],
                    'PIN_TYPE': pins['TYPE'],
                    'EXPIRES': pins['EXPIRES'],
                }
            }
        }
    }
    db.write_user_data(username, user_data)
    return user_data

    # check if db record is success #FIXME
