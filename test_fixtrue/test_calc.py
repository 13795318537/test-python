import pytest
import allure


@allure.feature('类的allure')
class TestCalc:
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @pytest.mark.add
    @pytest.mark.run(order=2)
    # @pytest.mark.parametrize(('a', 'b', 'exp'), add_dates, ids=addmyid_dates)
    def test_one(self, get_add_dates, get_calc):
        with allure.step('此处为第二个执行'):
            pass
        result = None
        try:
            result = get_calc.add(get_add_dates[0], get_add_dates[1])
            if isinstance(result, float):
                assert round(result, len(str(get_add_dates[2]).split(".")[1]))
        except Exception as e:
            print(e)
        pytest.assume(result == get_add_dates[2])

    @pytest.mark.div
    @pytest.mark.run(order=1)
    # @pytest.mark.parametrize(('a', 'b', 'exp'), div_dates, ids=divmyid_dates)
    def test_two(self, get_calc, get_div_dates):
        with allure.step('此处是第一个执行'):
            pass
        result = get_calc.div(get_div_dates[0], get_div_dates[1])
        if isinstance(result, float):
            assert round(result, 2) == get_div_dates[2]
        pytest.assume(result == get_div_dates[2])
