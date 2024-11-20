import allure
import requests
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('проверка сайта QA Tools')
@allure.feature('проверка заполнения формы')
def test_text_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")

    elements_form_first = [
        (driver.find_element(By.ID, 'userName'), 'userName', 'юзер нейм'),
        (driver.find_element(By.ID, 'userEmail'), 'userEmail', 'test@gmail.com'),
        (driver.find_element(By.ID, 'currentAddress'), 'currentAddress', 'валидный текст'),
        (driver.find_element(By.ID, 'permanentAddress'), 'permanentAddress', 'валидный текст')
    ]

    for elements, elements_text, elements_send_keys in elements_form_first:
        with allure.step(f'поля "{elements_text}" на отображение'):
            check.is_true(elements.is_displayed())
            elements.send_keys(elements_send_keys)

    with allure.step('прокликивание кнопки Submit'):
        driver.execute_script('window.scrollBy(0, 400);')
        driver.find_element(By.ID, 'submit').click()

    with allure.step('проверка наличия формы'):
        check.is_true(driver.find_element(By.ID, 'output').is_displayed(), 'форма не создана')

    elements_form_second = [
        (driver.find_element(By.ID, 'userName'), 'userName'),
        (driver.find_element(By.ID, 'userEmail'), 'userEmail'),
        (driver.find_element(By.XPATH,
            "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[3]"), 'currentAddress'),
        (driver.find_element(By.XPATH,
            "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[4]"), 'permanentAddress')
    ]

    for elements, elements_text in elements_form_second:
        with allure.step(f'проверка полей"{elements_text}"на отображение и правильность заполнения'):
            check.is_true(elements.is_displayed())

    url = 'https://demoqa.com/text-box'
    headers = {}
    response = requests.request('GET', url, headers=headers)
    data_response = response.json()
    check.equal(data_response['userName'], 'юзер нейм')
    check.equal(data_response['userEmail'], 'test@gmail.com')
    check.equal(data_response['/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[3]'],'валидный текст')
    check.equal(data_response['/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[4]'],'валидный текст')
    driver.close()
    driver.quit()