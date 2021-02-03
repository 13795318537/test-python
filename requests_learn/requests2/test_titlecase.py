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
    updata_myid = dates['updata_datas']['myid']
    delete_data = dates['delete_datas']['delete']
    delete_myid = dates['delete_datas']['myid']
    check1_data = dates['check1_datas']['check1']
    check1_myid = dates['check1_datas']['myid']


class Test_title():
    def setup_class(self):
        conf = yaml.safe_load(open("conf.yml", encoding='utf-8'))
        secret = conf["titlesecret"]
        self.title = Title_Api(secret)

    @pytest.mark.parametrize(("tagname", "tagid", "as_tagid"), create_date, ids=create_myid)
    def test_case_create(self, tagname, tagid, as_tagid):
        r = self.title.create_title(tagname, tagid)
        r1 = self.title.get_title_list()
        # assert r1['taglist'][-1]['tagid'] == 49
        ass_tagid = self.title.jsonpath_res(r1, f"$..taglist[?(@.tagid== {as_tagid})].tagid")[0]
        print(ass_tagid)
        if r['errcode'] == 0:
            assert ass_tagid == as_tagid
        else:
            r['errcode'] == 40068

    @pytest.mark.parametrize(("tagname", "tagid"), updata_data, ids=updata_myid)
    def test_case_update(self, tagname, tagid):
        r = self.title.update_title(tagname, tagid)
        r1 = self.title.get_title_list()
        # assert r1['taglist'][0]['tagid'] == 33
        tagname_list = self.title.jsonpath_res(r1, "$..tagname")
        assert tagname in tagname_list
        assert r['errcode'] == 0

    @pytest.mark.parametrize(("tagid"), delete_data, ids=delete_myid)
    def test_case_delete(self, tagid):
        r = self.title.delete_title(tagid)
        r1 = self.title.get_title_list()
        print(r1)
        tagid_d = self.title.jsonpath_res(r1, "$..tagid")
        assert tagid not in tagid_d
        assert r['errcode'] == 0

    @pytest.mark.parametrize(("tagid"), check1_data, ids=check1_myid)
    def test_case_checklist(self, tagid):
        r = self.title.get_title_list()
        assert r['errcode'] == 0
        check_list = self.title.jsonpath_res(r, "$..tagid")
        print(check_list)
        assert tagid in check_list
        r = json.dumps(r)
        print(r)
