from pprint import pprint
import random
import requests
import logging

SESSION = random.randint(10000, 99999)
TIMEOUT = 30
AUTH_TIMEOUT = 900

USR_INFO_1 = 'https://demo.epay.bg/xdev/api/user/info?'
USR_INFO_2 = 'https://demo.epay.bg/xdev/api/user/info/pins?'
USR_INFO_3 = 'https://demo.epay.bg/xdev/api/user/info/pins/balance?'

DEVICEID = '1510691760'
TOKEN = '78935936003423892015399874824155'
APPID = '6609898197243081281733444125044765054179316360618564706359682755'


def send_recv_req(url, data):
    r = requests.get(f'{url}{data}')
    r.json()

#    pprint(r.json())
    return(r.json())


def general_user_info():
    get_user_info = f'{USR_INFO_1}'
    get_user_info_params = f'APPID={APPID}&DEVICEID={DEVICEID}&TOKEN={TOKEN}'
    user_info = send_recv_req(get_user_info, get_user_info_params)

    pprint(user_info['userinfo'])
#    pprint(user_info)


general_user_info()


def get_user_pay_instrum():
    get_user_pins = f'{USR_INFO_2}'
    get_user_pins_params = f'APPID={APPID}&DEVICEID={DEVICEID}&TOKEN={TOKEN}'
    user_info = send_recv_req(get_user_pins, get_user_pins_params)

#    pprint(user_info['userinfo'])
    pprint(user_info)


get_user_pay_instrum()
