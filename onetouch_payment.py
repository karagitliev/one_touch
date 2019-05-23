from pprint import pprint
import requests
import onetouch_config as cfg


def send_recv(url, params):
    r = requests.post(url, data=params)

    r_json = r.json()
    return r_json


def payment():

    params = {
        'APPID': cfg.APPID,
        'DEVICEID': cfg.DEVICEID,
        'TOKEN': cfg.TOKEN,
        'TYPE': 'send'
    }

    # Get payment identificator
    r_json = send_recv(cfg.PAY_GET_ID, params)
    print('\n----\nGet payment indentificator')
    pprint(r_json)

    # should add if status OK here
    payment_id = r_json['payment']['ID']

    # Check params entered by user
    params.update(
        {
            'ID': payment_id,
            'AMOUNT': 100,
            'RCPT': cfg.KIN,
            'RCPT_TYPE': 'KIN',
            'DESCRIPTION': 'Test',
            'REASON': 'Testing app',
            'PINS': cfg.PIN,
            'SHOW': 'KIN',
        }
    )

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
        'DEVICEID': cfg.DEVICEID,
        'TOKEN': cfg.TOKEN,
        'ID': payment_id,
    }
    r_json = send_recv(cfg.PAY_CHECK_STATUS, params)
    print('\n----\nCheck money send status')
    pprint(r_json)


payment()
