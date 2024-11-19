from selenium import webdriver
import pytest
import allure
import time
import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.story('Проверка сайта')
@allure.feature('Проверка заполнения формы')
def test_text_box():
    driver = webdriver.Chrome()
    driver.set_window_size(1066660, 20666660)
    driver.get("https://demoqa.com/text-box")

    with allure.step('Проверка поля "userName"'):
        input_user_name = driver.find_element(By.ID, 'userName')
        check.is_true(input_user_name.is_displayed(), 'Инпута нет на экарне')

    with allure.step('Ввод текста в поле "userName"'):
        input_user_name.send_keys('Мой первый текст')

    driver.close()
    driver.quit()
