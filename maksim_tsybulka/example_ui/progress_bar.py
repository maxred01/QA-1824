""""Импорирование библиотек """
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер
driver = webdriver.Chrome()

# Переходим на страницу с прогресс-баром
driver.get("https://demoqa.com/progress-bar")

# Ожидаем загрузки страницы
time.sleep(2)

# Находим кнопку "Start"
start_button = driver.find_element(By.XPATH, "//button[text()='Start']")

# Нажимаем на кнопку "Start"
start_button.click()

# Ожидаем завершения загрузки
progress_bar = driver.find_element(By.XPATH, "//div[@role='progressbar']")
while progress_bar.get_attribute("aria-valuenow") != "100":
    time.sleep(0.1)

# Проверяем, что загрузка завершена
assert progress_bar.get_attribute("aria-valuenow") == "100"

# Закрываем браузер
driver.quit()
