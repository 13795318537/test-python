import os
import time
import pytest
import yaml
import allure

from codeself.query import QueryApi

yaml_file_path = os.path.dirname(__file__) + "/citycode.yml"

with open(yaml_file_path, encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    citycode = dates['city']['ccode']
    qqcode = dates['qq']['code']
    qqid = dates['qq']['myid']

@allure.feature("测试类1")
class Testyiqin(QueryApi):
    def setup_class(self):
        self.query = QueryApi()


    @allure.story("测试方法1")
    @pytest.mark.repeat(3)
    @pytest.mark.parametrize('cc', citycode)
    def test_anhui(self, cc):
        with allure.step('步骤1'):
            print("buzhou1")
        r = self.s_query()
        # print(r)
        ass_list = self.query.jsonpath_res(r, "$..city_id")
        print(ass_list)
        assert cc in ass_list
        assert r['reason'] == 'success!'

    @allure.story("测试方法12")
    @pytest.mark.parametrize(('key', 'qq'), qqcode, ids=qqid)
    def test_qq1(self, key, qq):
        r = self.qq_yun(key, qq)
        print(r)
        if r['reason'] == 'success!':
            assert r['error_code'] == 0
        elif r['reason'] == '错误的请求参数':
            assert r['error_code'] == 216602

