from requests_learn.requests2.Base_api import Base_Api


class WeWork(Base_Api):
    def __init__(self, secret):
        self.token = self.get_token(secret)

    def get_token(self, secret):
        date = {'method': 'get',
                'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                'params': {
                    'corpid': 'ww98266325a26bd2fa',
                    'corpsecret': secret}
                }
        r = self.send(date)
        return r.json()['access_token']
