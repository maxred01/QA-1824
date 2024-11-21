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

    driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
    driver.find_element(By.XPATH, '(//button[@class="rct-collapse rct-collapse-btn"])[2]').click()
    driver.find_element(By.XPATH, '//label[@for="tree-node-notes"]').click()
    len_elements = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

    time.sleep(2)
    check.is_true(driver.find_element(By.XPATH, '//input[@id="tree-node-notes"]').is_selected())
    check.equal(len(len_elements), 10)

    driver.close()
    driver.quit()
