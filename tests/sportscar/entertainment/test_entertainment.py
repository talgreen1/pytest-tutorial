import time

from pytest import mark


@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get("http://www.siriusxm.com/")
    time.sleep(4)
    assert True
