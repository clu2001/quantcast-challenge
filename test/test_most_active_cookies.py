import most_active_cookie
import pytest

# function testing for the case of no arguments, which is handled by argparse
def test_empty_arguments():
    with pytest.raises(SystemExit) as sys_exit:
        most_active_cookie.check_argument_validity([])
    assert sys_exit.type == SystemExit
    assert sys_exit.value.code == 2

# function testing if there are no cookies in the cookie log from the target date 
def test_no_cookies_on_date():
    with pytest.raises(Exception) as exception_info:
        most_active_cookie.get_cookies_list_on_target_date("../cookie_log.csv", "2018-12-10")
    assert exception_info.value.args[0] == "No available cookies found for target date"

# function testing if get_cookies_list_on_target_date returns list of all cookies on 
# given date 
def test_cookies_list():
    
    list_of_cookies = most_active_cookie.get_cookies_list_on_target_date("../cookie_log.csv", "2018-12-09")
    expected_output = ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']
    list_of_cookies2 = most_active_cookie.get_cookies_list_on_target_date("../cookie_log.csv", "2018-12-08")
    expected_output2 = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']

    assert list_of_cookies == expected_output
    assert list_of_cookies2 == expected_output2

# function testing if get_most_frequent_cookies returns list of most frequent cookies
def test_most_frequent_cookies():

    cookies_on_target_date = ['4sMM2LxV07bPJzwf']
    cookies_on_target_date2 = ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']

    list_of_cookies = most_active_cookie.get_most_frequent_cookies(cookies_on_target_date)
    expected_output = ['4sMM2LxV07bPJzwf']
    list_of_cookies2 = most_active_cookie.get_most_frequent_cookies(cookies_on_target_date2)
    expected_output2 = ['AtY0laUfhglK3lC7']

    assert list_of_cookies == expected_output
    assert list_of_cookies2 == expected_output2


