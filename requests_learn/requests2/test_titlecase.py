import json
import os

import pytest
import yaml
from requests_learn.requests2.title import Title_Api

yaml_file_path = os.path.dirname(__file__) + "/conf.yml"

with open(yaml_file_path, encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    create_date = dates['create_dates']['create']
    create_myid = dates['create_dates']['myid']
    updata_data = dates['updata_datas']['updata']
    update_myid = dates['updata_datas']['myid']

class Test_title():
    def setup_class(self):
        conf = yaml.safe_load(open("conf.yml"))
        secret = conf["titlesecret"]
        self.title = Title_Api(secret)

    @pytest.mark.parametrize(("tagname","tagid","as_tagid"), create_date, ids=create_myid)
    def test_case_create(self, tagname, tagid,as_tagid):
        r = self.title.create_title(tagname, tagid)
        r1 = self.title.get_title_list()
        # assert r1['taglist'][-1]['tagid'] == 49
        ass_tagid = self.title.jsonpath_res(r1, f"$..taglist[?(@.tagid== {as_tagid})].tagid")[0]
        print(ass_tagid)
        assert ass_tagid == as_tagid
        assert r['errcode'] == 0

    @pytest.mark.parametrize(("tagname","tagid"), updata_data, ids=update_myid)
    def test_case_update(self, tagname, tagid):
        r = self.title.update_title(tagname, tagid)
        r1 = self.title.get_title_list()
        assert r['errcode'] == 0
        # assert r1['taglist'][0]['tagid'] == 33
        tagname_list = self.title.jsonpath_res(r1, "$..tagname")
        tagid_list = self.title.jsonpath_res(r1, "$..taglist[?(@.tagid==38)].tagname")[0]
        assert tagname in tagname_list
        assert tagid_list == 'python7'

    @pytest.mark.parametrize("tagid", [600])
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

