import pytest
import yaml


class TestDate:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("test_yaml.yaml")))
    def test_date(self, a, b):
        print("**********************")
        print(a + b)
