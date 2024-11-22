import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('test site')
@allure.feature('test checkbox')
def test_accordion():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/accordian")

    time.sleep(1)

    driver.execute_script('window.scrollBy(0, 300);')

    time.sleep(2)

    widgets_click_one = driver.find_element(By.ID, 'section1Heading')
    widgets_click_one_text = driver.find_element(By.ID, 'section1Content')
    check.is_true(widgets_click_one_text.is_displayed(), 'No text')
    widgets_click_one.click()

    driver.execute_script('window.scrollBy(0, 150);')
    time.sleep(2)

    widgets_click_two = driver.find_element(By.ID, 'section2Heading')
    widgets_click_two_text = driver.find_element(By.ID, 'section2Content')
    widgets_click_two.click()
    check.is_true(widgets_click_two_text.is_displayed(), 'No text')
    time.sleep(1)
    widgets_click_two.click()
    time.sleep(2)

    driver.execute_script('window.scrollBy(0, 150);')
    time.sleep(2)

    widgets_click_three = driver.find_element(By.ID, 'section3Heading')
    widgets_click_three.click()
    time.sleep(2)
    widgets_click_three_text = driver.find_element(By.ID, 'section3Content')
    check.is_true(widgets_click_three_text.is_displayed(), 'No text')
    widgets_click_three.click()
    time.sleep(2)

    driver.close()
    driver.quit()









