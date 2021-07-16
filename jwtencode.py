import jwt
import time
import json
import os
from pathlib import Path

# 生成token的关键三个参数
_ISSUER_ID = ""
_KEY_ID = ""
_PRIVATE_KEY = ""

# 初始化config.json的参数值
def _initConfigJsonFile():
    file_path = os.getcwd() + '/config.json'
    with open(file_path, mode='r', encoding='utf8') as f_json:
        config_dict = json.load(f_json)
        global _ISSUER_ID
        _ISSUER_ID = config_dict['ISSUER_ID']
        global _KEY_ID
        _KEY_ID = config_dict['KEY_ID']
        temp_p8file_path = config_dict['AUTHKEY_PATH']

    with open(temp_p8file_path, mode='r') as f:
        global _PRIVATE_KEY
        _PRIVATE_KEY = f.read()

# 生成token值
def _creatAuthToken():
    _initConfigJsonFile()
    if len(_ISSUER_ID) == 0 or len(_KEY_ID) == 0 or len(_PRIVATE_KEY) == 0:
        print("❌[Error]: 请确认config.json文件中的参数配置正确")
        return
    encoded = jwt.encode(
        {
            "iss": _ISSUER_ID,
            "exp": int(time.time()) + 20 * 60,
            "aud": "appstoreconnect-v1"
        },
        _PRIVATE_KEY,
        algorithm="ES256",
        headers={"kid": _KEY_ID}
    )
    with open('token',mode='w+') as f_token:
        f_token.write(encoded)
    return str(encoded)

def getAuthToken(is_recreate = False):
    # 如果是需要重新获取的话,直接生成返回
    if is_recreate:
        return _creatAuthToken()
    # 不需要重新生成的话,先判断有没有之前生成好的token值
    token_file = Path("token")
    if token_file.is_file():
        with open(token_file, mode='r', encoding='utf8') as token:
            return token.read()
    else:
       return _creatAuthToken()

if __name__ == '__main__':
    print("")