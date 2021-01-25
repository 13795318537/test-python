import requests


class WeWork():
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': 'ww98266325a26bd2fa',
            'corpsecret': 'nfsyvLVCC1Kf0so6XEOQXYKv9j7eJyOYgF4b5n5sdno'
        }
        r = requests.request(method='get', url=url, params=params)
        return r.json()['access_token']
