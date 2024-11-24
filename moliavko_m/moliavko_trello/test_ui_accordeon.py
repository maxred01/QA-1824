import time
import pytest_check as check
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title('UI тесты')
@allure.feature('Проверка accordian')
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Mishael")

def test_accordian():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/accordian")

    driver.find_element(By.ID, "section1Heading").click()
    check.is_true(driver.find_element(By.ID, "section1Content").is_displayed())
    time.sleep(1)
    driver.find_element(By.ID, "section2Heading").click()
    check.is_true(driver.find_element(By.ID, "section2Content").is_displayed())
    time.sleep(1)
    driver.find_element(By.ID, "section3Heading").click()
    check.is_true(driver.find_element(By.ID, "section3Content").is_displayed())
    time.sleep(1)

    driver.close()
    driver.quit()
