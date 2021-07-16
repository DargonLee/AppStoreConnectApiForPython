import request_core
import api

def create_a_certificate(csrContent, certificateType="IOS_DEVELOPMENT"):
    """
    创建一个证书
    :param csrContent: Macos通过钥匙串创建的那个csr文件
    :param certificateType:  取值类型如下
    # IOS_DEVELOPMENT
    # IOS_DISTRIBUTION
    # MAC_APP_DISTRIBUTION
    # MAC_INSTALLER_DISTRIBUTION
    # MAC_APP_DEVELOPMENT
    # DEVELOPER_ID_KEXT
    # DEVELOPER_ID_APPLICATION
    # DEVELOPMENT
    # DISTRIBUTION
    :return: 请求结果
    """

    data = {
        "data": {
            "attributes": {
                "certificateType": certificateType,
                "csrContent": csrContent
            },
            "type": "certificates"
        }
    }
    result = request_core.POST(api.Certificate_API, data)
    print(result.text)
    return result

def list_and_download_certificates():
    """
    下载证书
    :return: 请求结果
    """
    data = {
        "fields[certificates]": "certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber",
        "filter[id]": "",
        "filter[serialNumber]": "",
        "limit": 200,
        "sort": "certificateType, -certificateType, displayName, -displayName, id, -id, serialNumber, -serialNumber",
        "filter[certificateType]": "",
        "filter[displayName]": ""
    }
    result = request_core.GET(api.Certificate_API, data)
    print(result.text)
    return result

def read_and_download_certificate_information(id):
    """
    读取并下载证书信息
    :param id: 证书id
    :return: 请求结果
    """
    data = {
        "fields[certificates]": "certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber"
    }
    result = request_core.GET(api.Certificate_API + '/' + id, data)
    print(result.text)
    return result

def revoke_a_certificate(id):
    """
    删除证书
    :param id: 证书id
    :return: 请求结果
    """
    result = request_core.DELETE(api.Certificate_API + '/' + id)
    print(result.text)
    return result

if __name__ == '__main__':
    print("")
    revoke_a_certificate("123")