# test Hoster

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver = driver
    driver.get("https://hoster.by")
    driver.find_element(By.XPATH, "//div[@id='menu-item']/span").click()

test_selenium()