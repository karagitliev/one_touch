from time import sleep
import requests
import urllib.parse
import onetouch_config as cfg


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    if req.status_code == requests.codes.ok:
        req_json = req.json()
        if req_json['status'] == 'OK':
            return req_json
        else:
            failcount = 0
            while req_json['status'] != 'OK':
                sleep(3)
                failcount += 3
                req = requests.get(url + query_string)
                req_json = req.json()
                if failcount > cfg.AUTH_TIMEOUT:
                    exit(f'{req_type} TIMEOUT')
            if req_json['status'] == 'OK':
                return req_json
            else:
                exit(f'{req_type} TIMEOUT')
    # add else in case of http status != 200 #FIXME
