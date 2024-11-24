""""Импорирование библиотек """
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер chrome и переходим на страницу https://demoqa.com/upload-download
driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

# Загружаем файл
upload_input = driver.find_element(By.ID, "uploadFile")
upload_input.send_keys("/path/to/image.jpg")
time.sleep(2)

# Проверяем, что файл загружен
uploaded_file = driver.find_element(By.ID, "uploadedFilePath").text
assert uploaded_file != "", "Файл не был загружен"

# Закрываем браузер
driver.quit()
