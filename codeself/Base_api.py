import requests
from jsonpath import jsonpath


class BaseApi:
    def request_send(self, date):
        return requests.request(**date)

    def jsonpath_res(self, ojb, expr):
        return jsonpath(ojb, expr)