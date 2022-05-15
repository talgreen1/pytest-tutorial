from selenium import webdriver
from selenium.webdriver.common.by import By


def test_1():
    driver = webdriver.Firefox()
    driver.get("http://www.controlup.com")
    assert "Python" in driver.title
    driver.find_element(By.XPATH, "/div[2]/div/p[1]/input[1]").send_keys("admin")
    driver.find_element(By.XPATH, "/div[2]/div/p[1]/input[2]").send_keys("qwe45tg")
    driver.find_element(By.XPATH, "/div[2]/div/p[1]/div").click()
    assert "Hello World" in driver.find_element(By.XPATH, "/body").text

    assert "_disabled" in driver.find_element(By.XPATH, "./input").get_attribute("class")

    driver.find_element(By.XPATH, "/div[2]/div/p[1]/div").click()
    assert driver.current_url.endswith("login")

    driver.close()
