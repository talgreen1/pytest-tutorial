from pytest import fixture
from selenium import webdriver

import json

def load_test_data(path):
    with open(path) as data_file:
        json.load()

# @fixture(params=[webdriver.Chrome, webdriver.Firefox()])
# def browser(request):
#     driver = request.param
#     drvr = driver()
#     yield drvr
#     drvr.quit()