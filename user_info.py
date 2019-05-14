from pprint import pprint
import random
import requests

import urllib.parse

SESSION = random.randint(10000, 99999)
TIMEOUT = 30
AUTH_TIMEOUT = 900

USR_BASE_URL = 'https://demo.epay.bg/xdev/api/user/'

DEVICEID = '1510691760'
TOKEN = '78935936003423892015399874824155'
APPID = '6609898197243081281733444125044765054179316360618564706359682755'


def send_recv_req(url, params):
    query_string = urllib.parse.urlencode(params)
    r = requests.get(url + query_string)
    print(url + query_string)
    r.json()

    # shoul check if there is answer here, or answer is correct

    return(r.json())


def general_user_info():
    params = {
        'APPID': APPID,
        'DEVICEID': DEVICEID,
        'TOKEN': TOKEN,
    }
    url = USR_BASE_URL + 'info?'
    user_info = send_recv_req(url, params)

    print('\n### General user info ###')
    pprint(user_info['userinfo'])


general_user_info()


def get_user_pay_instrum_balance(pins):
    print(pins)
    params = {
        'APPID': APPID,
        'DEVICEID': DEVICEID,
        'TOKEN': TOKEN,
        'PINS': pins,
    }
    url = USR_BASE_URL + 'info/pins/balance?'
    user_info_pins_balance = send_recv_req(url, params)

    print('\n### User payment instruments balance ###')
    pprint(user_info_pins_balance)


def get_user_pay_instrum():
    params = {
        'APPID': APPID,
        'DEVICEID': DEVICEID,
        'TOKEN': TOKEN,
    }
    url = USR_BASE_URL + 'info/pins?'
    user_info_pins = send_recv_req(url, params)

    print('\n### User payment instruments info ###')
    pprint(user_info_pins)

    pins_info = get_user_pay_instrum_balance(user_info_pins['payment_instruments'][0]['ID'])


get_user_pay_instrum()
