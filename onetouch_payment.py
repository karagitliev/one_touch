import time
from pprint import pprint
import onetouch_config as cfg
import onetouch_db_handler as db
import onetouch_send_recv as send


def get_taxes(username, amount, data):
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': data['DEVICEID'],
        'TOKEN': data['TOKEN'],
        'TYPE': 'send'
    }

    r_json = send.send_recv(cfg.PAY_GET_ID, params, 'GET ID')
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

    r_json = send.send_recv(cfg.PAY_CHECK_INP, params, 'GET TAXES')

    tax = r_json['payment']['PAYMENT_INSTRUMENTS'][0]['TAX']
    total = r_json['payment']['PAYMENT_INSTRUMENTS'][0]['TOTAL']
    params['AMOUNT'] = amount

    return(tax, total, params)


def payment(username, data):
    # Actual money send
    r_json = send.send_recv(cfg.PAY_MONEY_SEND, data, 'MONEYSEND')
    print('\n----\nActual money send')
    pprint(r_json)

    check_status(username, data)


def check_status(username, data):
    # Check money send status
    params = {
        'APPID': cfg.APPID,
        'DEVICEID': data['DEVICEID'],
        'TOKEN': data['TOKEN'],
        'ID': data['ID'],
    }
    r_json = send.send_recv(cfg.PAY_CHECK_STATUS, params, 'CHECK STATUS')
    print('\n----\nCheck money send status')
    pprint(r_json)

    # FIXME add if status OK here, then write to database
    r_json['TRANS_DATE'] = time.time()
    user_payment = {
        r_json['payment']['NO']: r_json,
    }
    db.write_user_data(username, user_payment, cfg.USERS_PAYMENTS)
