from ..frequentCookies import most_active_cookie


def testCookiesList():
    
    listOfCookies = most_active_cookie.getCookiesListOnTargetDate("cookie_log.csv", "2018-12-09")
    expectedOutput = ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7']
    listOfCookies2 = most_active_cookie.getCookiesListOnTargetDate("cookie_log.csv", "2018-12-08")
    expectedOutput2 = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']

    assert listOfCookies == expectedOutput
    assert listOfCookies2 == expectedOutput2












