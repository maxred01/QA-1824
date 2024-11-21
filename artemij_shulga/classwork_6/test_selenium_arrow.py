''' Test checkbox '''
from selenium import webdriver
import pytest
import allure
import time
import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



@allure.story('Test checkbox')
@allure.feature('Check button')
def test_text_box():
    """ testing checkbox"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")
    check_arrow_click = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    check_arrow_click.click()
    time.sleep(2)

    check_arrow_two = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
    check_arrow_two.click()
    time.sleep(2)

    check_arrow_three = driver.find_element(By.XPATH, '//*[@id="tree-node"]'
                                                      '/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]')
    check_arrow_three.click()
    time.sleep(2)

    check_arrow_notes = driver.find_element(By.XPATH, '//*[@id="tree-node-notes"]')
    check.is_true(check_arrow_notes.is_selected())

    driver.close()
    driver.quit()

