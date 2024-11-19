from selenium import webdriver
import pytest
import allure
import time
import pytest_check as check
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@allure.story('Проверка сайта')
@allure.feature('Проверка заполнения формы')
def test_test_box():
    driver = webdriver.Chrome()
    driver.set_window_size(1920,1080)
    driver.get("https://demoqa.com/text-box")

    with allure.step('Проверка поля "userName"'):
        input_user_name = driver.find_element(By.ID, 'userName')
        check.is_true(input_user_name.is_displayed(), 'Инпута нет на экарне')

    with allure.step('Ввод текста в поле "userName"'):
        input_user_name.send_keys('Мой первый текст')

    with allure.step('Проверка поля "Email"'):
        input_email = driver.find_element(By.ID, 'userEmail')
        input_email.send_keys('a@a.com')

    with allure.step('Проверка поля "адресс"'):
        input_current_adress = driver.find_element(By.ID, 'currentAddress')
        input_current_adress.send_keys('pushkina-kolotushkina')

    with allure.step('Проверка поля "перманент адресс"'):
        input_pa = driver.find_element(By.ID, 'permanentAddress')
        input_pa.send_keys('pushkina-kolotushkina')

    with allure.step('Проверка кнопки'f'submit'):
        output_data = driver.find_element(By.ID, 'submit')
        output_data = output_data.click()



    time.sleep(3)

    driver.close()
    driver.quit()
