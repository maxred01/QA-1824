import time
import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('Проверка сайта')
@allure.feature('Проверка заполнения формы')
def test_text_box():
    """Тест проверки работоспособности формы"""

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")

    elements_form = [
        (driver.find_element(By.ID, 'userName'), 'userName', 'Мой первый текст'),
        (driver.find_element(By.ID, 'userEmail'), 'userEmail', 'test@test.com'),
        (driver.find_element(By.ID, 'currentAddress'), 'currentAddress', 'Мой первый текст'),
        (driver.find_element(By.ID, 'permanentAddress'), 'permanentAddress', 'Мой первый текст')
    ]

    for elements, elements_text, elements_send_keys in elements_form:
        with allure.step(f'Поля "{elements_text}" на отображение'):
            time.sleep(1)
            check.is_true(elements.is_displayed())
            elements.send_keys(elements_send_keys)

    with allure.step('Нажатие на кноку Submit'):
        time.sleep(2)
        driver.execute_script('window.scrollBy(0, 300);')
        driver.find_element(By.ID, 'submit').click()

    with allure.step('Првоерка, что форма успешно заполнена'):
        check.is_true(driver.find_element(By.ID, 'output').is_displayed(), 'Формы не создана')

        with allure.step('Првоерка, что текст в ответе формы совпадает с веденным'):
            elements_form = [
                (driver.find_element(By.XPATH, '//p[@id="name"]').text, 'Мой первый текст'),
                (driver.find_element(By.XPATH, '//p[@id="email"]').text, 'test@test.com'),
                (driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text, 'Мой первый текст'),
                (driver.find_element(By.XPATH, '//p[@id="permanentAddress"]').text, 'Мой первый текст')
            ]
            for elements, elements_text in elements_form:
                check.greater(elements.find(elements_text), -1)

        time.sleep(5)

    driver.close()
    driver.quit()

