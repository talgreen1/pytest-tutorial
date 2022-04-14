from pytest import mark


@mark.ui
@mark.smoke
@mark.engine
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get("https://www.caranddriver.com/features/a26962316/how-a-car-works/")
    assert True
