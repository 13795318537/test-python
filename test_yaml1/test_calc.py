import pytest
import yaml

from test_yaml1 import calc
from test_yaml1.calc import Calculator

with open("calc_y.yml", encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    add_dates = dates['add']['dates']
    addmyid_dates = dates['add']['myid']
    div_dates = dates['div']['dates']
    divmyid_dates = dates['div']['myid']


class TestCalc:

    def setup(self):
        self.calc = Calculator()
        print('方法测试开始')

    def teardown(self):
        print('方法测试结束')

    def setup_class(self):
        print('类测试开始')

    def teardown_class(self):
        print('类测试结束')

    @pytest.mark.parametrize(('a', 'b', 'exp'), add_dates, ids=addmyid_dates)
    def test_one(self, a, b, exp):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            assert round(result, 2) == exp
        else:
            assert result == exp

    @pytest.mark.parametrize(('a', 'b', 'exp'), div_dates, ids=divmyid_dates)
    def test_two(self, a, b, exp):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            assert round(result, 2) == exp
        else:
            assert result == exp
