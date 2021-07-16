import request_core
import api


def register_new_bundle_id(name, identifier):
    """
    注册一个新的bundleId
    :param name: 名称
    :param identifier: bundleId标识符 比如:com.xxx.app
    :return: 请求结果
    """
    data = {
        "data": {
            "attributes": {
                "name": name,
                "identifier": identifier,
                "platform": api.Base_Platform,
                "seedId": ""
            },
            "type": "bundleIds"
        }
    }
    result = request_core.POST(api.Bundle_Id_API, data)
    print(result.text)
    return result


def modify_a_bundle_id(id, name):
    """
    更新bundle的名称
    :param id: bundle_id
    :param name: 需要修改的名称
    :return: 请求结果
    """
    data = {
        "data": {
            "attributes": {
                "name": name
            },
            "id": id,
            "type": "bundleIds"
        }
    }
    result = request_core.PATCH(api.Bundle_Id_API + '/' + id, data)
    print(result.text)
    return result

def delete_a_bundle_id(id):
    """
    删除bundle_id
    :param id: bundle_id
    :return: 请求结果
    """
    result = request_core.DELETE(api.Bundle_Id_API + '/' + id)
    print(result.text)
    return result

def get_bundle_id_list():
    """
    获取当前账号的所有bundle_id列表
    :return: 请求结果
    """
    data = {
        "filter[platform]": api.Base_Platform,
        "limit": 100
    }
    result = request_core.GET(api.Bundle_Id_API, data)
    print(result.text)
    return result

def read_bundle_id_information(id):
    """
    获取bundle_id的信息
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "filter[platform]": api.Base_Platform,
        "limit": 100
    }
    result = request_core.GET(api.Bundle_Id_API + '/' + id, data)
    print(result.text)
    return result

def read_app_information_of_bundle_id(id):
    """
    获取某个bundle_id的App信息
    [string]
    Possible values: appInfos, appStoreVersions, availableInNewTerritories,
    availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups,
    betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration,
    endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids,
    name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku
    :param id: 包名
    :return: 请求结果
    """
    data = {
        "fields[apps]": ""
    }
    result = request_core.GET(api.Bundle_Id_API + '/' + id + "/app")
    print(result.text)
    return result

def get_all_profiles_for_a_bundle_id(id):
    """
    获取某个bundle_id的所有描述文件
    :param id: bundle_id
    Query Parameters
        limit
        integer
        Maximum: 200
        fields[profiles]
        [string]
        Possible values: bundleId, certificates, createdDate,
        devices, expirationDate, name, platform, profileContent,
        profileState, profileType, uuid
    :return: 请求结果
    """
    data = {
        "filter[profiles]": "profileType",
        "limit": 200
    }
    result = request_core.GET(api.Bundle_Id_API + '/' + id + "/profiles", data)
    print(result.text)
    return result

def get_all_capabilities_for_a_bundle_id(id):
    """
    获取某个bundle_id所有的Capabilities
    :param id: bundle_id
    :return: 请求结果
    """
    data = {
        "filter[bundleIdCapabilities]": "capabilityType",
        "limit": 200
    }
    result = request_core.GET(api.Bundle_Id_API + '/' + id + "/bundleIdCapabilities", data)
    print(result.text)
    return result

if __name__ == '__main__':
    # register_new_bundle_id("vender_test", "com.uusafe.sdk")
    get_all_profiles_for_a_bundle_id("com.uusafe.sdk")