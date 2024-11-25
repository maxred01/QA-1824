import time
import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('test site')
@allure.feature('test checkbox')

def test_checkbox():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")

    check_box_home_click = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    check_box_home_click.click()
    time.sleep(1)

    check_box_desctop_click = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]'
                                                            '/span/button')
    check_box_desctop_click.click()
    time.sleep(1)

    check_box_notes = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]'
                                                    '/span/label/span[1]')
    check_box_notes.click()
    time.sleep(1)

    check_box_notes_click = driver.find_element(By.XPATH, '//*[@id="tree-node-notes"]')
    check.is_true(check_box_notes_click.is_selected())

    driver.close()
    driver.quit()
