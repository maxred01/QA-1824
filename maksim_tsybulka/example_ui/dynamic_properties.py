""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем веб-драйвер Chrome и переходим на страницу
driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

# Ждем, пока кнопка будет доступна для нажатия
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
button.click()

# Проверяем, что все кнопки доступны для нажатия
buttons = driver.find_elements(By.CSS_SELECTOR, "button[onclick='myFunction()']")
for button in buttons:
    assert button.is_enabled()

# Закрываем веб-драйвер
driver.quit()
