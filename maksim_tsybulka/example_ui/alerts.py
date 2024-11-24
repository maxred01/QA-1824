""""Импорирование библиотек """
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер браузера
driver = webdriver.Chrome()

# Переходим на страницу https://demoqa.com/alerts
driver.get("https://demoqa.com/alerts")

# Находим кнопку "Click me" и кликаем на нее
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "alertButton"))
)
button.click()

# Ждем, пока появится alert
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
assert alert.text == "You clicked a button"

# Принимаем alert
alert.accept()

# Находим кнопку "Click me" и кликаем на нее
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "timerAlertButton"))
)
button.click()

# Ждем, пока появится alert
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Ждем 5 секунд, чтобы alert успел исчезнуть
time.sleep(5)

# Принимаем alert
alert.accept()

# Находим кнопку "Click me" и кликаем на нее
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "confirmButton"))
)
button.click()

# Ждем, пока появится confirm
confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
assert confirm.text == "Do you confirm action?"

# Отменяем confirm
confirm.dismiss()

# Находим кнопку "Click me" и кликаем на нее
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "promtButton"))
)
button.click()

# Ждем, пока появится prompt
prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
assert prompt.text == "Please enter your name"

# Вводим текст в prompt
prompt.send_keys("Test User")

# Принимаем prompt
prompt.accept()

# Находим элемент "Prompt text" и проверяем, что он содержит введенный текст
prompt_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "promptResult"))
)
assert prompt_text.text == "You entered: Test User"

# Закрываем браузер
driver.quit()
