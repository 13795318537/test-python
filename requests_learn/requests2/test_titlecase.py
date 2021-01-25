import pytest

from requests_learn.requests2.title import Title_Api


class Test_title():
    def setup_class(self):
        self.title = Title_Api()

    @pytest.mark.parametrize("tagname,tagid", [('python18', 38)])
    def test_case1(self, tagname, tagid):
        r = self.title.create_title(tagname, tagid)
        r1 = self.title.get_title_list()
        assert r1['taglist'][-1]['tagid'] == 38
        print(r)
        assert r['errcode'] == 0

    @pytest.mark.parametrize("tagname,tagid", [('42342342', 33)])
    def test_case_update(self, tagname, tagid):
        r = self.title.update_title(tagname, tagid)
        r1 = self.title.get_title_list()
        print(r)
        assert r['errcode'] == 0
        assert r1
