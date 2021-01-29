import requests
from requests_learn.requests2.wework import WeWork


class Title_Api(WeWork):
    def create_title(self, tagname, tagid):
        date = {'method': 'post',
                'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/create',
                'params': {'access_token': self.token},
                'json': {
                    "tagname": tagname,
                    "tagid": tagid
                }
                }
        r = self.send(date)
        return r.json()

    def update_title(self, tagname, tagid):
        date = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/update',
            'params': {
                'access_token': self.token
            },
            'json': {
                "tagid": tagid,
                "tagname": tagname
            }
        }
        r = self.send(date)
        return r.json()

    def delete_title(self, tagid):
        date = {'method': 'get',
                'url': "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
                'params': {
                    'access_token': self.token,
                    'tagid': tagid
                }
                }
        r = self.send(date)
        return r.json()

    def get_title_list(self):
        date = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/list',
            'params': {
                'access_token': self.token
            }
        }
        r = self.send(date)
        return r.json()
