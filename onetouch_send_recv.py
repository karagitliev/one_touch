import sys
import requests
import urllib.parse
import onetouch_app as app

from time import sleep


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    if req.status_code == requests.codes.ok:
        return(req.json())
    else:
        failcount = 0
        while req.status_code != requests.codes.ok:
            sleep(3)
            failcount += 3
            req = requests.get(url + query_string)
            if failcount > app.AUTH_TIMEOUT:
                pass
        if req.status_code == requests.codes.ok:
            return(req.json())
        else:
            sys.exit('AUTHORISATION TIMEOUT')
