import pytest
import yaml
import selenium


# 列表【】参数化
class TestDate:
    # @pytest.mark.parametrize(('age', "name"), yaml.safe_load(open('test_yaml.yaml', encoding='utf-8')))
    @pytest.mark.parametrize(('name', 'age'), [('qew', '22')])
    def test_date(self, name, age):

        print("**********************")
        print(name, '今天', age)


