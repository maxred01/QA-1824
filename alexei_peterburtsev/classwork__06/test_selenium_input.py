import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('Validation Site')
@allure.feature('Validation input fields')

def test_text_box():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")

    user_test_name = 'Masha'
    user_test_email = 'Masha@belarus.by'
    user_cur_aderess = 'Masha sity'
    user_perm_adress = 'Rep Masha'

    form_ele = [
        (driver.find_element(By.ID, 'userName'), 'userName', user_test_name),
        (driver.find_element(By.ID, 'userEmail'), 'userEmail', user_test_email),
        (driver.find_element(By.ID, 'currentAddress'), 'currentAddress', user_cur_aderess),
        (driver.find_element(By.ID, 'permanentAddress'), 'permanentAddress', user_perm_adress)
    ]

    for elements, elements_text, elements_send_keys in form_ele:
        with allure.step(f'Fields "{elements_text}" on show'):
            time.sleep(1)
            check.is_true(elements.is_displayed())
            elements.send_keys(elements_send_keys)

    with allure.step('Submin press'):
        time.sleep(1)
        driver.execute_script('window.scrollBy(0, 450);')
        driver.find_element(By.ID, 'submit').click()

    with allure.step('Check user form is True'):
        check.is_true(driver.find_element(By.ID, 'output').is_displayed(), 'Form is False')

    with allure.step('Check "name" is True'):
        check.is_true(driver.find_element(By.ID, 'name').is_displayed(), '"name" is False')

    with allure.step('Check "email" is True'):
        check.is_true(driver.find_element(By.ID, 'email').is_displayed(), '"email" is False')

    with allure.step('Check "currentAddress" is True'):
        check.is_true(driver.find_element(By.ID, 'currentAddress').is_displayed(),
                      '"currentAddress" is False')

    with allure.step('Check "permanentAddress" is True'):
        check.is_true(driver.find_element(By.ID, 'permanentAddress').is_displayed(),
                      '"permanentAddress" is False')

    user_name = driver.find_element(By.XPATH, '//*[@id="name"]').text
    user_email = driver.find_element(By.XPATH, '//*[@id="email"]').text

    with allure.step('Check "name" is True'):
        check.equal(user_name, f'Name:{user_test_name}', '"name" is False')

    with allure.step('Check "email" is True'):
        check.equal(user_email, f'Email:{user_test_email}', '"email" is False')

    time.sleep(2)
    driver.close()
    driver.quit()
