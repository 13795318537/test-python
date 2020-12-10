

class TestCalc:

    # @pytest.mark.parametrize(('a', 'b', 'exp'), add_dates, ids=addmyid_dates)
    def test_one(self, get_calc, get_add_dates):
        result = get_calc.add(get_add_dates[0], get_add_dates[1])
        if isinstance(result, float):
            assert round(result, 2) == get_add_dates[2]
        else:
            assert result == get_add_dates[2]

    # @pytest.mark.parametrize(('a', 'b', 'exp'), div_dates, ids=divmyid_dates)
    def test_two(self, get_calc, get_div_dates):
        result = get_calc.div(get_div_dates[0],get_div_dates[1])
        if isinstance(result, float):
            assert round(result, 2) == get_div_dates[2]
        else:
            assert result == get_div_dates[2]
