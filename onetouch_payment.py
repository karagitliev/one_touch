from pprint import pprint
import requests
import onetouch_config as config
import onetouch_urls as urls


def payment():

    params = {
        'APPID': config.APPID,
        'DEVICEID': config.DEVICEID,
        'TOKEN': config.TOKEN,
        'TYPE': 'send'
    }

    # Get payment identificator
    r = requests.post(urls.PAY_GET_ID, data=params)
    r_json = r.json()
    print('\n----\nGet payment indentificator')
    pprint(r_json)

    # should add if status OK here
    payment_id = r_json['payment']['ID']

    # Check params entered by user
    params.update(
        {
            'ID': payment_id,
            'AMOUNT': 100,
            'RCPT': config.KIN,
            'RCPT_TYPE': 'KIN',
            'DESCRIPTION': 'Test',
            'REASON': 'Testing app',
            'PINS': config.PIN,
            'SHOW': 'KIN',
        }
    )

    r = requests.post(urls.PAY_CHECK_INP, data=params)
    r_json = r.json()
    print('\n----\nCheck user input and taxes')
    pprint(r_json)

    # Actual money send
    r = requests.post(urls.PAY_MONEY_SEND, data=params)
    r_json = r.json()
    print('\n----\nActual money send')
    pprint(r_json)

    # Check money send status
    params = {
        'APPID': config.APPID,
        'DEVICEID': config.DEVICEID,
        'TOKEN': config.TOKEN,
        'ID': payment_id,
    }
    r = requests.post(urls.PAY_CHECK_STATUS, data=params)
    r_json = r.json()
    print('\n----\nCheck money send status')
    pprint(r_json)


payment()
