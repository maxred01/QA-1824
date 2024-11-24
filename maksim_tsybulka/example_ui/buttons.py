""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://demoqa.com/buttons")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "doubleClickBtn")))

# Нахождение элементов на странице
single_click_btn = driver.find_element_by_id("singleClickBtn")
double_click_btn = driver.find_element_by_id("doubleClickBtn")
right_click_btn = driver.find_element_by_id("rightClickBtn")

# Нажатие на кнопки
single_click_btn.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))

action = webdriver.ActionChains(driver)
action.double_click(double_click_btn).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doubleClickMessage")))

action.context_click(right_click_btn).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rightClickMessage")))

# Закрытие браузера
driver.quit()
