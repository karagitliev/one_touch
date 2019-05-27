import time
from pprint import pprint
import requests
import onetouch_config as cfg
import onetouch_db_handler as db


def send_recv(url, params):
    r = requests.post(url, data=params)

    r_json = r.json()
    return r_json


def get_taxes(username, amount, data):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': data['DEVICEID'],
        'TOKEN': data['TOKEN'],
        'TYPE': 'send'
    }

    r_json = send_recv(cfg.PAY_GET_ID, params)
    params.update(
        {
            'ID': r_json['payment']['ID'],
            'AMOUNT': amount,
            'RCPT': cfg.KIN,
            'RCPT_TYPE': 'KIN',
            'DESCRIPTION': 'Test',
            'REASON': 'Testing app',
            'PINS': data['PIN_ID'],
            'SHOW': 'KIN',
        }
    )

    r_json = send_recv(cfg.PAY_CHECK_INP, params)

    tax = r_json['payment']['PAYMENT_INSTRUMENTS'][0]['TAX']
    total = r_json['payment']['PAYMENT_INSTRUMENTS'][0]['TOTAL']
    params['AMOUNT'] = amount

    return(tax, total, params)


def payment(username, params):
    r_json = send_recv(cfg.PAY_CHECK_INP, params)
    print('\n----\nCheck user input and taxes')
    pprint(r_json)

   # Actual money send
    r_json = send_recv(cfg.PAY_MONEY_SEND, params)
    print('\n----\nActual money send')
    pprint(r_json)

   # Check money send status
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': params['DEVICEID'],
        'TOKEN': params['TOKEN'],
        'ID': params['ID'],
    }
    r_json = send_recv(cfg.PAY_CHECK_STATUS, params)
    print('\n----\nCheck money send status')
    pprint(r_json)

    # FIXME add if status OK here, then write to database
    r_json['TRANS_DATE'] = time.time()
    user_payment = {
        r_json['payment']['NO']: r_json,
    }
    db.write_user_data(username, user_payment, cfg.USERS_PAYMENTS)
