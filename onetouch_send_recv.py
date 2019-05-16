import requests
import urllib.parse


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    req = requests.get(url + query_string)

    if req.status_code == requests.codes.ok:
        return req.json()
