import time
import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('проверка сайта')
@allure.feature('проверка чекбоксов')
def test_check_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")

    driver.find_element(By.XPATH, "(//*[@class='rct-collapse rct-collapse-btn'])[1]").click()
    driver.find_element(By.XPATH, "(//*[@class='rct-collapse rct-collapse-btn'])[2]").click()
    driver.find_element(By.XPATH, "(//*[@class='rct-checkbox'])[3]").click()
    check_box_notes = driver.find_element(By.XPATH, "//*[@id='tree-node-notes']")
    len_elements = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

    time.sleep(2)

    check.is_true(check_box_notes.is_selected())
    check.is_true(len(len_elements), 6)



    driver.close()
    driver.quit()