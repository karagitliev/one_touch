from pprint import pprint
import random
import requests
import logging

SESSION = random.randint(10000, 99999)
TIMEOUT = 30
AUTH_TIMEOUT = 900

AUTH_START = 'https://demo.epay.bg/xdev/mobile/api/start?'
AUTH_VERIFY = 'https://demo.epay.bg/xdev/api/api/code/get?'
AUTH_GET_TOKEN = 'https://demo.epay.bg/xdev/api/api/token/get?'

APPID = '6609898197243081281733444125044765054179316360618564706359682755'
USERNAME = 'a_t_xyTgiDz90Z'
PASSWORD = '8UP5slwW1E'

DEVICEID = '1510691760'
TOKEN = '78935936003423892015399874824155'


def authorization():
    key = random.randint(10000000, 99999999)
    deviceid = random.randint(1000000000, 9999999999)

    r = requests.get(f'{AUTH_START}APPID={APPID}&DEVICEID={deviceid}&KEY={key}')
    r.json()

    pprint(r.json())


authorization()
