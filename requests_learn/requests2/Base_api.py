import requests


class Base_Api():
    def send(self, date):
        return requests.request(**date)