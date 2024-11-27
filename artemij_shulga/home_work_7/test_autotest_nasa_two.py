import time
import allure
import pytest_check as check
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Autotests")
@allure.feature("Test ssl and status code")
@allure.description("check: ssl certificate passed and status code 200")
@allure.tag("Autotest", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("QA", "Artemij Shulga")
@allure.link("https://www.nasa.gov/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

def test_status_code_nasa():
    """ testing status code """
    url = 'https://www.nasa.gov/'

    headers = {}

    response = requests.request('GET', url, headers=headers)

    with allure.step("nasa status check code"):
        check.equal(response.status_code, 200,
                    f'status code is not equal to 200.Status code is {response.status_code}')


def test_ssl_certificate_exists():
    """ testing ssl certificate """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.sslshopper.com/ssl-checker.html#hostname=")

    with allure.step("enter link us NASA"):
        driver.find_element(By.ID, "hostname").send_keys("https://www.nasa.gov/")
        time.sleep(1)

    with allure.step("click on button CHECK SSL"):
        driver.find_element(By.ID, "checkButton").click()
        driver.execute_script("window.scrollBy(0,850);")
        time.sleep(1)

    with allure.step("certificate verification NASA"):
        ssl = driver.find_element(By.XPATH, '//*[@id="checkData"]/table[1]/tbody/tr[7]/td[1]')
        check.is_true(ssl.is_displayed(), 'this site dont have ssl_certificate')

    time.sleep(5)
    driver.close()
    driver.quit()
