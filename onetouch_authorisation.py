import random
import urllib.parse
import webbrowser
import requests
from sys import exit
from time import sleep

import onetouch_urls as urls
import onetouch_config as config


SESSION = random.randint(10000, 99999)


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    if req.status_code == requests.codes.ok:
        req_json = req.json()
        if req_json['status'] == 'OK':
            return(req_json)
        else:
            failcount = 0
            while req_json['status'] != 'OK':
                sleep(3)
                failcount += 3
                req = requests.get(url + query_string)
                req_json = req.json()
                if failcount > config.AUTH_TIMEOUT:
                    sys.exit(f'{req_type} TIMEOUT')
            if req_json['status'] == 'OK':
                return(req_json)
            else:
                sys.exit(f'{req_type} TIMEOUT')


def authorisation():
    key = random.randint(10000000, 99999999)
    deviceid = random.randint(1000000000, 9999999999)

    params = {
        'APPID': config.APPID,
        'DEVICEID': deviceid,
        'KEY': key,
    }

    # This opens a browser and opens ePay.bg for user authorisation
    req_string = urllib.parse.urlencode(params)
    webbrowser.open_new(urls.AUTH_START + req_string)

    # Get code
    req_type = 'GET CODE'
    resp = send_recv(urls.AUTH_VERIFY, params, req_type)
    params['CODE'] = resp['code']
    print(f'GET CODE SUCCESS\n{resp}')

    # Actual TOKEN receipt
    req_type = 'AUTHORISATION'
    resp = send_recv(urls.AUTH_GET_TOKEN, params, req_type)
    print(f'\nGET TOKEN SUCCESS\n{resp}')


authorisation()