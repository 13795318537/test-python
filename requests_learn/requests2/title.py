import requests
from requests_learn.requests2.wework import WeWork

class Title_Api(WeWork):
    def create_title(self,tagname,tagid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create'
        token = {'access_token': self.token}
        payload = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.request(method='post', url=url, params=token, json=payload)
        return r.json()

    def update_title(self,tagid,tagname):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update'
        access_token = {
            'access_token': self.token
        }
        payload = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = requests.request(method='post', url=url, params=access_token, json=payload)
        return r.json()


    def delete_title(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete'
        tagid = 25
        params = {
            'access_token': self.token,
            'tagid': tagid
        }
        r = requests.request(method='get', url=url, params=params)
        return r.json()


    def get_title_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        params = {
            'access_token': self.token
        }
        r = requests.request(method='get', url=url, params=params)
        return r.json()
