from pprint import pprint
import random

import onetouch_app as app
import onetouch_log as log
import onetouch_urls as urls
import onetouch_send_recv as req


SESSION = random.randint(10000, 99999)


def authorisation():
    key = random.randint(10000000, 99999999)
    deviceid = random.randint(1000000000, 9999999999)

    params = {
        'APPID': app.APPID,
        'DEVICEID': deviceid,
        'KEY': key,
    }

    url = urls.AUTH_START
    req_type = 'auth_start'
    authorisation = req.send_recv(url, params, req_type)

    print('\n### Authorisation ###')
    pprint(authorisation)


authorisation()
