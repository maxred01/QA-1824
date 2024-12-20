import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('test site')
@allure.feature('test checkbox')
def test_accordion():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/modal-dialogs")
    time.sleep(1)
    driver.execute_script('window.scrollBy(0, 300);')
    time.sleep(1)
    modal_click_small = driver.find_element(By.ID, 'showSmallModal')
    modal_click_small.click()
    time.sleep(3)
    modal_click_small_close = driver.find_element(By.ID, 'closeSmallModal')
    modal_click_small_close.click()
    modal_click_small = driver.find_element(By.ID, 'showSmallModal')
    modal_click_small.click()
    time.sleep(2)
    modal_click_small_close = driver.find_element(By.XPATH, ' //button[@class="close"]')
    modal_click_small_close.click()
    time.sleep(3)
    modal_click_large = driver.find_element(By.ID, 'showLargeModal')
    modal_click_large.click()
    time.sleep(3)
    modal_click_large_close = driver.find_element(By.ID, 'closeLargeModal')
    modal_click_large_close.click()
    time.sleep(3)
    modal_click_large = driver.find_element(By.ID, 'showLargeModal')
    modal_click_large.click()
    time.sleep(2)
    modal_click_large_close = driver.find_element(By.XPATH, '//button[@class="close"]')
    modal_click_large_close.click()
    time.sleep(2)
    driver.close()
    driver.quit()