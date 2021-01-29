import requests
from requests_learn.requests2.Base_api import Base_Api


class WeWork(Base_Api):
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        date = {'method': 'get',
                'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                'params': {
                    'corpid': 'ww98266325a26bd2fa',
                    'corpsecret': 'nfsyvLVCC1Kf0so6XEOQXYKv9j7eJyOYgF4b5n5sdno'}
                }
        r = self.send(date)
        return r.json()['access_token']
