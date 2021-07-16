# AppStoreConnectApi For Python
> Apple AppStoreConnectApi 接口Python版本封装

#### 环境准备
- 安装PyJWT
```
git clone https://github.com/jpadilla/pyjwt/
cd pyjwt-master
python3 setup.py install

或者 pip install PyJWT

```
**保证PyJWT版本为`2.1.0`以上版本**
***
- 填写config.json文件参数

具体参数获取参考:`https://www.jianshu.com/p/ea3a37a997f4`
```
例如:
{
  "ISSUER_ID": "69a6de8a-1105-47e3-e053-5b8c7c11",
  "KEY_ID": "65V4AP592V",
  "AUTHKEY_PATH": "./AuthKey.p8"
}
```