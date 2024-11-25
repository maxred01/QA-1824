""" тестирование аккордеона """
import time
import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('Тестирование UI')
@allure.feature('Тестирование Аккордеона')

def test_accordian():
    """ функция тестирования аккордеона """

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/accordian")
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(2)

    # закрыть 1-й аккордеон
    acc1_off = driver.find_element(By.XPATH, '//*[@id="section1Heading"]')
    acc1_off.click()
    time.sleep(1)

    # проверить, что 1-й аккордеон закрыт
    with allure.step('Проверка 1-го аккордиона после закрытия'):
        check.is_false(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[1]/div[2]').is_displayed(),
                       '1-й аккордион не закрылся')

    # открыть 1-й аккордеон
    acc1_on = driver.find_element(By.XPATH, '//*[@id="section1Heading"]')
    acc1_on.click()
    time.sleep(1)

    # проверить, что 1-й аккордеон открыт
    with allure.step('Проверка 1-го аккордиона после открытия'):
        check.is_true(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[1]/div[2]').is_displayed(),
                      '1-й аккордион не открылся')

    time.sleep(2)
    driver.execute_script('window.scrollBy(0, 375);')
    time.sleep(2)

    # открыть 2-й аккордион
    acc2_on = driver.find_element(By.XPATH, '//*[@id="section2Heading"]')
    acc2_on.click()
    time.sleep(1)

    # проверить, что 2-й аккордеон открыт
    with allure.step('Проверка 2-го аккордиона после открытия'):
        check.is_true(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[2]/div[2]').is_displayed(),
                      '2-й аккордион не открылся')

    # закрыть 2-й аккордеон
    acc2_off = driver.find_element(By.XPATH, '//*[@id="section2Heading"]')
    acc2_off.click()
    time.sleep(1)

    # проверить, что 2-й аккордеон закрыт
    with allure.step('Проверка 2-го аккордиона после закрытия'):
        check.is_false(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[2]/div[2]').is_displayed(),
                       '2-й аккордион не закрылся')

    time.sleep(2)
    driver.execute_script('window.scrollBy(0, 10);')
    time.sleep(2)

    # открыть 3-й аккордеон
    acc3_on = driver.find_element(By.XPATH, '//*[@id="section3Heading"]')
    acc3_on.click()
    time.sleep(1)

    # проверить, что 3-й аккордеон открыт
    with allure.step('Проверка 3-го аккордиона после открытия'):
        check.is_true(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[3]/div[2]').is_displayed(),
                      '3-й аккордион не открылся')

    # закрыть 3-й аккордеон
    acc3_off = driver.find_element(By.XPATH, '//*[@id="section3Heading"]')
    acc3_off.click()
    time.sleep(1)

    # проверить, что 3-й аккордеон закрыт
    with allure.step('Проверка 3-го аккордиона после закрытия'):
        check.is_false(driver.find_element(By.XPATH,
            '//*[@id="accordianContainer"]/div/div[3]/div[2]').is_displayed(),
                       '3-й аккордион не закрылся')

    time.sleep(3)
    driver.close()
    driver.quit()
