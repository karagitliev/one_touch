import requests
import urllib.parse


def send_recv(url, params, req_type):
    query_string = urllib.parse.urlencode(params)
    r = requests.get(url + query_string)
    print(url + query_string)
    r.json()

    return(r.json())
