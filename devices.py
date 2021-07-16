import request_core
import api


def register_a_new_device(name, udid):
    """
    注册一个设备到账号里面
    :param name: 设备名称
    :param udid: 设备的udid
    :return: 请求结果
    """
    data = {
        "data": {
            "attributes": {
                "name": name,
                "platform": api.Base_Platform,
                "udid": udid
            },
            "type": "devices"
        }
    }
    result = request_core.POST(api.Devices_API, data)
    print(result.text)
    return result

def get_devices_list():
    """
    获取当前账号的所有设备列表
    :return: 请求结果
    """
    data = {
        "filter[platform]": api.Base_Platform,
        "limit": 100
    }
    result = request_core.GET(api.Devices_API, data)
    print(result.text)
    return result

def read_device_information(id):
    """ id="36DU79L2GV"
    获取设备的详细信息
    :param id: 设备的id,可以通过 get_devices_list 的response里获得
    :return: 请求结果
    """
    result = request_core.GET(api.Devices_API + id)
    print(result.text)
    return result

def modify_a_registered_device(id, name, status="ENABLED"):
    """
    修改某个设备的名称或者状态
    :param id: 设备的id
    :param name: 设备名称
    :param status: 设备状态 取值: ENABLED or DISABLED
    :return: 请求结果
    """
    data = {
        "data": {
            "attributes": {
                "name": name,
                "status": status
            },
            "id": id,
            "type": "devices"
        }
    }
    result = request_core.PATCH(api.Devices_API + '/' + id, data)
    print(result.text)
    return result

if __name__ == '__main__':
    register_a_new_device("vender_test", "988caf5753f0d0a17a78236a388923e12a7981c3")
    # get_devices_list()
    # modify_a_registered_device("36DU79L2GV", "xxx")