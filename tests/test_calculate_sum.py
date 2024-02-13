from Pages.main import Main
from Testdata import test_data


def test_sum(app):

    main_obj = Main(app)
    num_1 = test_data.test_num
    num_2 = test_data.test_num
    main_obj.sum_numbers(num_1, num_2)
    result = main_obj.get_result_text()
    expected_rusult = str(num_1+num_2)
    assert result == expected_rusult
   