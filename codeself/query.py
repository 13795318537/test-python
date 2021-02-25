from codeself.Base_api import BaseApi


class QueryApi(BaseApi):
    def s_query(self):
        date = {'method': 'get',
                'url': 'http://apis.juhe.cn/springTravel/citys?key=10019',
                'params': '=&key=450a1fd80d1b76601dce27501077f7e8'
                }
        r = self.request_send(date)
        return r.json()

    def qq_yun(self, key, qq):
        date = {'method': 'post',
                'url': 'http://japi.juhe.cn/qqevaluate/qq',
                'data': {
                    'key': key,
                    'qq': qq
                }
                }
        r = self.request_send(date)
        return r.json()
