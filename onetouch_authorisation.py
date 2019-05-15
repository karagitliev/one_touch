import sys
import random
import requests
import webbrowser
import urllib.parse

from time import sleep

import onetouch_urls as urls
import onetouch_config as config


SESSION = random.randint(10000, 99999)


def send_recv(url, params):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    return(req.json())


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
    resp = send_recv(urls.AUTH_VERIFY, params)

    if resp['status'] == 'OK':
        print(f'GET CODE SUCCESS {resp}')
    else:
        failcount = 0
        while resp['status'] != 'OK':
            sleep(3)
            failcount += 3
            resp = send_recv(urls.AUTH_VERIFY, params)
            if failcount > config.AUTH_TIMEOUT:
                sys.exit('AUTHORISATION TIMEOUT')
        if resp['status'] == 'OK':
            print(f'GET CODE SUCCESS\n{resp}')
        else:
            sys.exit('AUTHORISATION TIMEOUT')

    params['CODE'] = resp['code']

    # Actual TOKEN receipt
    resp = send_recv(urls.AUTH_GET_TOKEN, params)
    if resp['status'] == 'OK':
        print('GET TOKEN SUCCESS')
    else:
        failcount = 0
        while resp['status'] != 'OK':
            sleep(3)
            failcount += 3
            resp = send_recv(urls.AUTH_GET_TOKEN, params)
            if failcount > config.AUTH_TIMEOUT:
                sys.exit('AUTHORISATION TIMEOUT')
        if resp['status'] == 'OK':
            print('GET TOKEN SUCCESS')
        else:
            sys.exit('AUTHORISATION TIMEOUT')

    print(f'GET TOKEN SUCCESS\n{resp}')


authorisation()
