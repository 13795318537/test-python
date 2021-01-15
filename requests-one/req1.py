import requests


class TestReq:

    # get基础请求
    def test_one(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.json())
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
        print(r.text)
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
