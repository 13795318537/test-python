import pytest
import yaml
import os
from test_fixtrue.calc import Calculator

yaml_file_path = os.path.dirname(__file__) + "/calc_y.yml"

with open(yaml_file_path, encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    add_dates = dates['add']['dates']
    addmyid_dates = dates['add']['myid']
    div_dates = dates['div']['dates']
    divmyid_dates = dates['div']['myid']


@pytest.fixture()
def get_calc():
    calc = Calculator()
    print('开始计算')
    yield calc
    print('结束')


@pytest.fixture(params=add_dates, ids=addmyid_dates)
def get_add_dates(request):
    date = request.param
    return date

@pytest.fixture(params=div_dates, ids=divmyid_dates)
def get_div_dates(request):
    date = request.param
    return date