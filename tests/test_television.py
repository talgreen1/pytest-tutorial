from pytest import mark


# @mark.parametrize('tv_brand', [
#     ('Samsung'),
#     ('LG'),
#     ('Sony')
# ])
# def test_television_turns_on(tv_brand):
#     print(f"{tv_brand} Turns on as expected")

#
# def test_browser_can_navigate_to_site(browser):
#     browser.get("http://www.google.com")


def test_television_turns_on(test_data):
    print(f"{test_data} Turns on as expected")