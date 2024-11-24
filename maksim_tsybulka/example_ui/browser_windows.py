""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер браузера
driver = webdriver.Chrome()

# Переходим на страницу https://demoqa.com/browser-windows
driver.get("https://demoqa.com/browser-windows")

# Находим кнопку "Click Here" и кликаем на нее
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "windowButton"))
)
button.click()

# Переключаемся на новое окно
driver.switch_to.window(driver.window_handles[1])

# Ждем, пока загрузится новая страница
WebDriverWait(driver, 10).until(EC.title_contains("ToolsQA"))

# Находим элемент "New Message Window" и кликаем на него
new_message_button = driver.find_element_by_id("sampleHeading")
new_message_button.click()

# Переключаемся на новую вкладку
driver.switch_to.window(driver.window_handles[2])

# Ждем, пока загрузится новая страница
WebDriverWait(driver, 10).until(EC.title_contains("Sample Iframe page"))

# Находим элемент "Your Message" и проверяем, что он отображается
your_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[text()='Your Message']"))
)
assert your_message.is_displayed()

# Закрываем браузер
driver.quit()
