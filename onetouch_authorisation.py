import random
import requests
import webbrowser
import urllib.parse
from sys import exit
from time import sleep

import onetouch_user_info as usr_info
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

    # Get code
    req_type = 'GET CODE'
    resp = send_recv(cfg.AUTH_VERIFY, params, req_type)
    params['CODE'] = resp['code']

    # Actual TOKEN receipt
    req_type = 'AUTHORISATION'
    resp = send_recv(cfg.AUTH_GET_TOKEN, params, req_type)

    # Get user payment instruments
    pins = usr_info.pay_instruments(deviceid, resp['TOKEN'])
    # Should add logic for more than 1 payment instrument #FIXME
    user_pins = {
        username: {
            'pins': {
                '1': {  # FIXME change this name
                    'KEY': key,
                    'NAME': pins['NAME'],
                    'CODE': params['CODE'],
                    'TOKEN': resp['TOKEN'],
                    'PIN_ID': pins['ID'],
                    'EXPIRES': pins['EXPIRES'],
                    'PIN_TYPE': pins['TYPE'],
                    'DEVICEID': deviceid,
                }
            }
        }
    }
    db.write_user_data(username, user_pins, cfg.USERS_PINS)
    db.create_user(username)

    # check if db record is success #FIXME

    get_user_info = usr_info.general_user_info(deviceid, resp['TOKEN'])
    user_info = {
        username: {
            'KIN': get_user_info['userinfo']['KIN'],
            'GSM': get_user_info['userinfo']['GSM'],
            'EMAIL': get_user_info['userinfo']['EMAIL'],
            'REAL_NAME': get_user_info['userinfo']['REAL_NAME'],
        }
    }
    db.write_user_data(username, user_info, cfg.USERS_DATA)
