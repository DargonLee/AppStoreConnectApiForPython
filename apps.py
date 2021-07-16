import request_core


def get_apps():
    result = request_core.GET("https://api.appstoreconnect.apple.com/v1/apps")
    print(result.text)
    return result

if __name__ == '__main__':
    result = request_core.GET("https://api.appstoreconnect.apple.com/v1/apps")
    print(result.text)