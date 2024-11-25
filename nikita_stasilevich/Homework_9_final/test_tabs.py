""""Импорирование библиотек """
import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.story('Проверка сайта')
@allure.feature('Проверка Tabs')
def test_tabs():
    """Тест проверки работоспособности Tab"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/tabs")
    driver.execute_script('window.scrollBy(0, 450);')
    time.sleep(2)
    # Кликаем вкладку Origin
    tabs_origin = driver.find_element(By.ID, 'demo-tab-origin')
    tabs_origin.click()
    time.sleep(2)
    check.is_true(tabs_origin.is_displayed())
    # Тут проверяем что он открыт(Origin)
    tabs_origin_text = driver.find_element(By.XPATH, '//div[@class="fade tab-pane active show"]')
    check.is_true(tabs_origin_text.is_displayed())
    time.sleep(2)
    # Кликаем вкладку Use
    tabs_use = driver.find_element(By.ID, 'demo-tab-use')
    tabs_use.click()
    time.sleep(2)
    check.is_true(tabs_use.is_displayed())
    #  Тут проверяем что он открыт(Use)
    tabs_use_text = driver.find_element(By.XPATH, '//div[@class="fade tab-pane active show"]')
    check.is_true(tabs_use_text.is_displayed())
    time.sleep(2)
    # Кликаем вкладку What
    tabs_what = driver.find_element(By.ID, 'demo-tab-what')
    tabs_what.click()
    time.sleep(2)
    check.is_true(tabs_what.is_displayed())
    # проверяем вкладку What
    tabs_what_text = driver.find_element(By.XPATH, '//div[@class="fade tab-pane active show"]')
    check.is_true(tabs_what_text.is_displayed())
    time.sleep(2)
    driver.close()
    driver.quit()