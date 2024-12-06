import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('Test UI accordian')
@allure.feature('Check accordian')
def test_accordian():
    """ testing accordian """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/accordian")

    first_tab = driver.find_element(By.ID, 'section1Heading')
    check_content_close = driver.find_element(By.XPATH, '//*[@class = "collapse show"]')
    first_tab.click()
    time.sleep(1)

    with allure.step("close the tab 'What is Lorem Ipsum?'"):
        check.is_false(check_content_close.is_displayed(), "content is not closed in 'What is Lorem Ipsum?'")
        time.sleep(3)

    first_tab.click()
    time.sleep(1)

    with allure.step("check for content in 'What is Lorem Ipsum?'"):
        check_content_one = driver.find_element(By.XPATH, '//*[@id="section1Content"]')
        check.is_true(check_content_one.is_displayed(), "no content in 'What is Lorem Ipsum?'")
        time.sleep(3)
        first_tab.click()
        driver.execute_script('window.scrollBy(0,200);')
        time.sleep(3)

    second_tab = driver.find_element(By.ID, 'section2Heading')
    second_tab.click()
    time.sleep(1)

    with allure.step("check for content in 'Where does it come from?'"):
        check_content_two = driver.find_element(By.XPATH, '//*[@id="section2Content"]')
        check.is_true(check_content_two.is_displayed(), "no content in 'Where does it come from?'")
        time.sleep(3)
        driver.execute_script('window.scrollBy(0,200);')

    second_tab.click()
    time.sleep(1)

    with allure.step("close the tab 'Where does it come from?'"):
        check.is_false(check_content_close.is_displayed(), "content is not closed in 'Where does it come from?'")
        time.sleep(3)

    third_tab = driver.find_element(By.ID, 'section3Heading')
    third_tab.click()
    time.sleep(1)

    with allure.step("check for content in 'Why do we use it?'"):
        check_content_three = driver.find_element(By.XPATH, '//*[@id="section3Content"]')
        check.is_true(check_content_three.is_displayed(), "no content in 'Why do we use it?'")
        time.sleep(3)
        third_tab.click()
        driver.execute_script('window.scrollBy(0,200);')
        time.sleep(3)

    with allure.step("close the tab 'Why do we use it?'"):
        check.is_false(check_content_close.is_displayed(), "content is not closed in 'Why do we use it?'")
        time.sleep(3)

    time.sleep(5)
    driver.close()
    driver.quit()
