from pytest import fixture

from selenium import webdriver


@fixture(scope="session")
def chrome_browser():
    browser = webdriver.Chrome("./chromedriver")
    return browser
