import pytest
import requests
from jsonpath import jsonpath

class TestReq:

    def setup_class(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': 'ww98266325a26bd2fa',
            'corpsecret': 'nfsyvLVCC1Kf0so6XEOQXYKv9j7eJyOYgF4b5n5sdno'
        }
        r = requests.request(method='get', url=url, params=params)
        self.token = r.json()['access_token']
        print(r.json())
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("tagname,tagid", [('python116', 311)])
    def test_create_title(self, tagname, tagid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create'
        token = {'access_token': self.token}
        payload = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.request(method='post', url=url, params=token, json=payload)
        # print(r.json())
        url1 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        params = {
            'access_token': self.token
        }
        r1 = requests.request(method='get', url=url1, params=params)
        ass_list = jsonpath(r1, "$..tagid")
        print(ass_list)
        assert r1.json()['taglist'][-1]['tagid'] == 31
        assert r.json()['errcode'] == 0

    def test_update_title(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update'
        access_token = {
            'access_token': self.token
        }
        payload = {
            "tagid": 41,
            "tagname": "UI111"
        }
        r = requests.request(method='post', url=url, params=access_token, json=payload)
        assert r.json()['errcode'] == 0

    def test_delete_title(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete'
        tagid = 25
        params = {
            'access_token': self.token,
            'tagid': tagid
        }
        r = requests.request(method='get', url=url, params=params)
        assert r.json()['errcode'] == 0

    def test_check_title(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        params = {
            'access_token': self.token
        }
        r = requests.request(method='get', url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == 0
