import random
import requests
import urllib.parse
from pprint import pprint

import onetouch_app as app
import onetouch_log as _log
import onetouch_urls as urls

SESSION = random.randint(10000, 99999)


def send_recv_req(url, params):
    query_string = urllib.parse.urlencode(params)
    r = requests.get(url + query_string)
    print(url + query_string)
    r.json()

    # shoul check if there is answer here, or answer is correct

    return(r.json())


def general_user_info():
    params = {
        'APPID': app.APPID,
        'DEVICEID': app.DEVICEID,
        'TOKEN': app.TOKEN,
    }
    url = urls.USR_INF_GEN
    user_info = send_recv_req(url, params)

    print('\n### General user info ###')
    pprint(user_info['userinfo'])


general_user_info()


def get_user_pay_instrum_balance(pins):
    params = {
        'APPID': app.APPID,
        'DEVICEID': app.DEVICEID,
        'TOKEN': app.TOKEN,
        'PINS': pins,
    }
    url = urls.USR_INF_BALANCE
    user_info_pins_balance = send_recv_req(url, params)

    print('\n### User payment instruments balance ###')
    pprint(user_info_pins_balance)


def get_user_pay_instrum():
    params = {
        'APPID': app.APPID,
        'DEVICEID': app.DEVICEID,
        'TOKEN': app.TOKEN,
    }
    url = urls.USR_INF_PINS
    user_info_pins = send_recv_req(url, params)

    print('\n### User payment instruments info ###')
    pprint(user_info_pins)

    pins_info = get_user_pay_instrum_balance(user_info_pins['payment_instruments'][0]['ID'])


get_user_pay_instrum()
