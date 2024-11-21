""""Импорирование библиотек """
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

    check_box_home_click = driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[1]')
    check_box_home = driver.find_element(By.XPATH, '//input[@id="tree-node-home"]')

    check_box_home_click.click()
    time.sleep(2)
    check.is_true(check_box_home.is_selected())

    driver.close()
    driver.quit()
