import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.story('Проверка сайта')
@allure.feature('Проверка чекбоксов')
def test_checkbox():
    """Тест проверки работоспособности чекбоксов"""
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://demoqa.com/checkbox")
    check_box_home_click = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    check_box_home_click.click()
    time.sleep(1)

    check_box_home_desctop = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
    check_box_home_desctop.click()
    time.sleep(1)

    check_box_home_notes = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]')
    check_box_home_notes.click()




    driver.close()
    driver.quit()