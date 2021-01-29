import json

import jsonpath
import pytest

from requests_learn.requests2.title import Title_Api


class Test_title():
    def setup_class(self):
        self.title = Title_Api()

    @pytest.mark.parametrize("tagname,tagid", [('python49', 49)])
    def test_case1(self, tagname, tagid):
        r = self.title.create_title(tagname, tagid)
        r1 = self.title.get_title_list()
        assert r1['taglist'][-1]['tagid'] == 49
        print(r1)
        assert r['errcode'] == 0

    @pytest.mark.parametrize("tagname,tagid", [('test15', 49)])
    def test_case_update(self, tagname, tagid):
        r = self.title.update_title(tagname, tagid)
        r1 = self.title.get_title_list()
        print(r1)
        assert r['errcode'] == 0
        # assert r1['taglist'][0]['tagid'] == 33
        tagname_list = jsonpath(r1, "$..tagname")
        assert tagname in tagname_list

    @pytest.mark.parametrize("tagid", [33])
    def test_case_delete(self, tagid):
        r = self.title.delete_title(tagid)
        r1 = self.title.get_title_list()
        print(r1)
        assert r['errcode'] == 0

    def test_case_checklist(self):
        r = self.title.get_title_list()
        assert r['errcode'] == 0
        r = json.dumps(r)
        print(r)
