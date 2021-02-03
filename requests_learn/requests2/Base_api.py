import requests
from jsonpath import jsonpath
from typing import List


class Base_Api():


    def send(self, date):
        return requests.request(**date)

    def jsonpath_res(self, ojb, expr):
        return jsonpath(ojb, expr)

    def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
    ) -> None:
        """Called after collection has been performed. May filter or re-order
        the items in-place.

        :param pytest.Session session: The pytest session object.
        :param _pytest.config.Config config: The pytest config object.
        :param List[pytest.Item] items: List of item objects.
        """
        for item in items:
            item.name = item.name.encode('utf-8').decode('unicode-escape')
            item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
