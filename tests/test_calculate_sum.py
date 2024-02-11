import config
from Pages.login_app import Login_to_App
from Pages.main import Main
from Testdata import test_data

def test_sum(app):

    # activate Chrome browser

    main_obj = Main(app)
    num_1 = test_data.numbers[0]
    num_2 = test_data.numbers[3]
    main_obj.sum_numbers(num_1, num_2)
    res = main_obj.get_result_text()
    expected_rus = str(num_1+num_2)
    assert res == expected_rus
   