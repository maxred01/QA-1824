''' Test register '''
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
    """ Testing register """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    input_user_name = driver.find_element(By.ID, 'userName')
    input_background = driver.find_element(By.ID, 'output')

    with allure.step('Проверка поля "userName"'):
        check.is_true(input_user_name.is_displayed(), 'Инпута нет на экарне')

    with allure.step('Ввод текста в поле "userName"'):
        time.sleep(1)
        input_user_name.send_keys('Avatar Aang - gyatso')

    with allure.step('Ввод текста в поле "userEmail"'):
        time.sleep(1)
        driver.find_element(By.ID, 'userEmail').send_keys("dfggddgd@email.com")

    with allure.step('Ввод текста в поле "currentAddress'):
        time.sleep(1)
        driver.find_element(By.ID, 'currentAddress').send_keys("привет, это я - твой единственный зритель")

    with allure.step('Ввод текста в поле "permanentAddress'):
        time.sleep(1)
        driver.find_element(By.ID, 'permanentAddress').send_keys('gyatso-code')

    with allure.step("Кликнуть на кнопку 'submit'"):
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,450);')
        driver.find_element(By.ID, 'submit').click()

    with allure.step("Проверка поле заявки 'class'"):
        check.is_true(input_background.is_displayed(), 'пользователь успешно зарегистрирован')

    with allure.step("Кликнуть на кнопку 'name'"):
        check.is_true(driver.find_element(By.ID, 'name'), 'name no register')

    with allure.step("Кликнуть на кнопку 'email'"):
        check.is_true(driver.find_element(By.ID, 'email'), 'email no register')

    with allure.step("Кликнуть на кнопку 'currentAddress'"):
        check.is_true(driver.find_element(By.ID, 'currentAddress'), 'currentAddress no register')

    with allure.step("Кликнуть на кнопку 'permanentAddress'"):
        check.is_true(driver.find_element(By.ID, 'permanentAddress'),'permanentAddress no register')

    name_user = driver.find_element(By.XPATH, '//*[@id="name"]').text
    email_user = driver.find_element(By.XPATH, '//*[@id="email"]').text
    currect_user = driver.find_element(By.XPATH, '//*[@id="currentAddress"]').text
    permanent_user = driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').text
    print(name_user, email_user, currect_user, permanent_user)

    time.sleep(5)
    driver.close()
    driver.quit()

