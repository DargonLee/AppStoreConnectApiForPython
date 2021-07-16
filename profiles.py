import request_core
import api

def create_a_profile(id, profileType="IOS_APP_DEVELOPMENT"):
    """
    创建一个描述文件
    profileType:
    [
        Possible values: IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC,
        IOS_APP_INHOUSE, MAC_APP_DEVELOPMENT, MAC_APP_STORE, MAC_APP_DIRECT,
        TVOS_APP_DEVELOPMENT, TVOS_APP_STORE, TVOS_APP_ADHOC, TVOS_APP_INHOUSE,
        MAC_CATALYST_APP_DEVELOPMENT, MAC_CATALYST_APP_STORE, MAC_CATALYST_APP_DIRECT
    ]
    :param id: 包名
    :param profileType: 描述文件类型
    :return: 请求结果
    """
    data = {
        "data": {
            "attributes": {
                "name": "",
                "profileType": profileType
            },
            "relationships": {
                "bundleId": {
                    "data": {
                        "id": id,
                        "type": "bundleIds"
                    }
                },
                "certificates": {
                    "data": {
                        "id": id,
                        "type": "certificates"
                    }
                },
                "devices": {
                    "data": {
                        "id": id,
                        "type": "devices"
                    }
                }
            },
            "type": "profiles"
        }
    }
    result = request_core.POST(api.Profiles_API, data)
    print(result.text)
    return result

def delete_a_profile(id):
    """
    删除一个包名的描述文件
    :param id: bundle_id
    :return: 请求结果
    """
    result = request_core.DELETE(api.Profiles_API + '/' + id)
    print(result.text)
    return result

def list_and_download_profiles():
    """

    link: https://developer.apple.com/documentation/appstoreconnectapi/list_and_download_profiles
    :return: 请求结果
    """
    data = {
        "fields[certificates]": "certificateType",
        "fields[devices]": "platform",
        "fields[profiles]": "profileType",
        "filter[id]": "",
        "include": "bundleId, certificates, devices",
        "limit": 200,
        "limit[certificates]": 50,
        "limit[devices]": 50,
        "sort": "id, -id, name, -name, profileState, -profileState, profileType, -profileType",
        "fields[bundleIds]": " app, bundleIdCapabilities, identifier, name, platform, profiles, seedId",
        "filter[profileState]": "ACTIVE",
        "filter[profileType]": "IOS_APP_DEVELOPMENT, IOS_APP_STORE, IOS_APP_ADHOC, IOS_APP_INHOUSE"
    }
    result = request_core.GET(api.Profiles_API, data)
    print(result.text)
    return result

def read_and_download_profile_information(id):
    """
    linke: https://developer.apple.com/documentation/appstoreconnectapi/read_and_download_profile_information
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "fields[certificates]": "certificateType",
        "fields[devices]": "platform",
        "fields[profiles]": "profileType",
        "include": "bundleId, certificates, devices",
        "fields[bundleIds]": "app, bundleIdCapabilities, identifier, name, platform, profiles, seedId",
        "limit[devices]": 50,
        "limit[certificates]": 50
    }
    result = request_core.GET(api.Profiles_API + '/' + id, data)
    print(result.text)
    return result

def read_the_bundle_id_in_a_profile(id):
    """
    获取某个bundle_id的描述文件信息
    link: https://developer.apple.com/documentation/appstoreconnectapi/read_the_bundle_id_in_a_profile
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "fields[bundleIds]": "app, bundleIdCapabilities, identifier, name, platform, profiles, seedId"
    }
    result = request_core.GET(api.Profiles_API + '/' + id + '/bundleId', data)
    print(result.text)
    return result

def list_all_certificates_in_a_profile(id):
    """
    获取某个描述文件的所有证书
    link: https://developer.apple.com/documentation/appstoreconnectapi/list_all_certificates_in_a_profile
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "limit": 200,
        "fields[certificates]": "certificateContent, certificateType, csrContent, displayName, expirationDate, name, platform, serialNumber"
    }
    result = request_core.GET(api.Profiles_API + '/' + id + '/certificates', data)
    print(result.text)
    return result

def list_all_devices_in_a_profile(id):
    """
    获取某个描述文件的所有设备
    link: https://developer.apple.com/documentation/appstoreconnectapi/list_all_devices_in_a_profile
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "limit": 200,
        "fields[devices]": "addedDate, deviceClass, model, name, platform, status, udid"
    }
    result = request_core.GET(api.Profiles_API + '/' + id + '/devices', data)
    print(result.text)
    return result


if __name__ == '__main__':
    print("")
    # delete_a_profile("com.sdk")
    # read_the_bundle_id_in_a_profile("123")
    # list_all_certificates_in_a_profile("123")