""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://demoqa.com/broken")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "broken_image")))

# Проверка изображения на странице
broken_image = driver.find_element_by_id("broken_image")
valid_image = driver.find_element_by_id("valid_image")
broken_link = driver.find_element_by_id("broken_link")

# Проверка сломанного изображения
if "broken_image" in broken_image.get_attribute("src"):
    print("Изображение содержит ошибку!")

# Проверка валидной ссылки на изображение
if "https://i.imgur.com/hKdG7kA.jpg" in valid_image.get_attribute("src"):
    print("Изображение отображается корректно!")
else:
    print("Изображение содержит ошибку!")

# Проверка сломанной ссылки
try:
    broken_link.click()
    print("Ссылка не сломана!")
except FileExistsError:
    print("Ссылка содержит ошибку!")

# Закрытие браузера
driver.quit()
