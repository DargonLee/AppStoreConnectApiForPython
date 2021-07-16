import requests
import json
import jwtencode

_token = "Bearer " + jwtencode.getAuthToken()
_headers = {
    "content-type": "application/json",
    "Authorization": _token
}

_session = requests.session()
_session.keep_alive = False

def _recreate_token():
    global _token
    _token = "Bearer " + jwtencode.getAuthToken(True)
    global _headers
    _headers = {
        "Authorization": _token
    }

def GET(url, data={}):
    print(url)
    print(data)
    print(_headers)
    response = _session.get(url, params=data, headers=_headers)
    # token授权失败 重新获取 再次发送请求
    if response.status_code == 401:
        _recreate_token()
        response = _session.get(url, params=data, headers=_headers)
    print("GET status code = " + str(response.status_code))
    return response

def POST(url, data={}):
    print(url)
    print(data)
    print(_headers)
    response = _session.post(url, data=json.dumps(data), headers=_headers)
    # token授权失败 重新获取 再次发送请求
    if response.status_code == 401:
        _recreate_token()
        response = _session.post(url, data=json.dumps(data), headers=_headers)
    print("POST status code = " + str(response.status_code))
    return response

def PATCH(url, data={}):
    print(url)
    print(data)
    print(_headers)
    response = _session.patch(url, data=json.dumps(data), headers=_headers)
    # token授权失败 重新获取 再次发送请求
    if response.status_code == 401:
        _recreate_token()
        response = _session.patch(url, data=data, headers=_headers)
    print("PATCH status code = " + str(response.status_code))
    return response

def DELETE(url, data={}):
    print(url)
    print(data)
    print(_headers)
    response = _session.delete(url, data=json.dumps(data), headers=_headers)
    # token授权失败 重新获取 再次发送请求
    if response.status_code == 401:
        _recreate_token()
        response = _session.delete(url, data=json.dumps(data), headers=_headers)
    print("DELETE status code = " + str(response.status_code))
    return response