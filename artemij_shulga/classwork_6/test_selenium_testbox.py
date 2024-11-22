import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('Site check')
@allure.feature('Checking the completion of the form')
def test_text_box():
    """ Testing register """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    input_user_name = driver.find_element(By.ID, 'userName')
    input_background = driver.find_element(By.ID, 'output')

    with allure.step("Field Validation userName"):
        check.is_true(input_user_name.is_displayed(), "Инпута нет на экарне")

    with allure.step("Entering text in a field userName"):
        time.sleep(1)
        input_user_name.send_keys('Avatar Aang - gyatso')

    with allure.step("Entering text in a field userEmail"):
        time.sleep(1)
        driver.find_element(By.ID, 'userEmail').send_keys('dfggddgd@email.com')

    with allure.step("Entering text in a field currentAddress"):
        time.sleep(1)
        driver.find_element(By.ID, 'currentAddress').send_keys('привет, это я - твой единственный зритель')

    with allure.step("Entering text in a field permanentAddress"):
        time.sleep(1)
        driver.find_element(By.ID, 'permanentAddress').send_keys('gyatso-code')

    with allure.step("Click on the button submit"):
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,450);')
        driver.find_element(By.ID, 'submit').click()

    with allure.step("Checking the application field class"):
        check.is_true(input_background.is_displayed(), 'user successfully registered')

    with allure.step("check field name"):
        check.is_true(driver.find_element(By.ID, 'name'), 'name no register')

    with allure.step("check field email"):
        check.is_true(driver.find_element(By.ID, 'email'), 'email no register')

    with allure.step("check field currentAddress"):
        check.is_true(driver.find_element(By.ID, 'currentAddress'), 'currentAddress no register')

    with allure.step("check field permanentAddress"):
        check.is_true(driver.find_element(By.ID, 'permanentAddress'), 'permanentAddress no register')

    name_user = driver.find_element(By.XPATH, '//*[@id="name"]').text
    email_user = driver.find_element(By.XPATH, '//*[@id="email"]').text
    adress_user = driver.find_element(By.XPATH, '//*[@id="currentAddress"]').text
    permanent_user = driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').text
    print(name_user, email_user, adress_user, permanent_user)

    time.sleep(5)
    driver.close()
    driver.quit()
