import most_active_cookie

# function testing if get_cookies_list_on_target_date returns list of all cookies on 
# given date 
def test_cookies_list():
    
    list_of_cookies = most_active_cookie.get_cookies_list_on_target_date("../cookie_log.csv", "2018-12-09")
    expected_output = ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']
    list_of_cookies2 = most_active_cookie.get_cookies_list_on_target_date("../cookie_log.csv", "2018-12-08")
    expected_output2 = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']

    assert list_of_cookies == expected_output
    assert list_of_cookies2 == expected_output2

# function testing if get_most_frequent_cookies returns 
def test_most_frequent_cookies():

    cookies_on_target_date = ['4sMM2LxV07bPJzwf']
    cookies_on_target_date2 = ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']

    list_of_cookies = most_active_cookie.get_most_frequent_cookies(cookies_on_target_date)
    expected_output = ['4sMM2LxV07bPJzwf']
    list_of_cookies2 = most_active_cookie.get_most_frequent_cookies(cookies_on_target_date2)
    expected_output2 = ['AtY0laUfhglK3lC7']

    assert list_of_cookies == expected_output
    assert list_of_cookies2 == expected_output2
    
if __name__ == "__main__":
    test_cookies_list()
    test_most_frequent_cookies()









