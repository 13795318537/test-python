import requests
from jsonpath import jsonpath
from typing import List


class Base_Api():
    def send(self, date):
        return requests.request(**date)

    def jsonpath_res(self, ojb, expr):
        return jsonpath(ojb, expr)


