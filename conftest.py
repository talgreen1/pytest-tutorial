from pytest import fixture

from selenium import webdriver


@fixture(scope="session")
def chrome_browser():
    browser = webdriver.Chrome("./chromedriver")
    yield browser

    #     teardown
    print("I'm tearing down this browser")
