import requests
from jsonpath import jsonpath
from hamcrest import *


class TestReq:

    def test_at(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            'corpid': 'ww98266325a26bd2fa',
            'corpsecret': 'nfsyvLVCC1Kf0so6XEOQXWfBS8MBggdL6xj5dzEXCPs'
        }
        r = requests.get(url=url, params=params)
        print(r.json())

    # get基础请求
    def test_one(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.json())
        print(r.text)
        print(r.status_code)
        assert r.status_code == 200

    # get带query请求
    def test_query(self):
        payload = {
            'name': 'charles',
            'age': 16
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    # post带data请求
    def test_post_form(self):
        payload = {
            'name': 'charles',
            'age': 16
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.json())
        assert r.status_code == 200

    '''
    上传文件
    files= {'file':open('文件路径','rb')}
    r = requests.post('url',files=files)
    带header
    headers = {'Content-Type':'application/json'}
    r = requests.post('url',headers=headers)
    cookies = dict(cookies_are='working')
    r = requests.post('url',cookies=cookies)
    '''

    def test_header(self):
        r = requests.post('https://httpbin.testing-studio.com/post', headers={'H': 'header demo'})
        print(r.text)
        assert r.status_code == 200

    # post_json请求
    def test_post_json(self):
        payload = {
            'name': 'charles',
            'age': 16
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['age'] == 16

    def test_one(self):
        r = requests.get('https://ceshiren.com/categories.json')
        assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'
        assert_that(
            r.json()['category_list']['categories'][0]['name'],
            equal_to('开源项目'))

    def test_cookie(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {'User-Agent': 'python-header'}
        cookies_data = {
            "cookies": "cookies_data_test",
            "tester": "zhu"
        }
        r = requests.get(url, headers=header, cookies=cookies_data, timeout=0.1)
        print(r.request.headers)

    # 认证
    def test_auth(self):
        from requests.auth import HTTPBasicAuth
        url = 'https://httpbin.testing-studio.com/basic-auth/apple/1234'
        r = requests.get(url, auth=HTTPBasicAuth("apple", "1234"))
        print(r.json())
        # print(r.headers)

    def test_111(self):
        from requests.auth import HTTPBasicAuth
        url = 'https://httpbin.testing-studio.com/basic-auth/apple/1234'
        r = requests.request(method='get', url=url, auth=HTTPBasicAuth("apple", "1234"))
        print(r.json())
