""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер браузера
driver = webdriver.Chrome()

# Переходим на страницу https://demoqa.com/frames
driver.get("https://demoqa.com/frames")

# Переключаемся на фрейм "Single Iframe"
driver.switch_to.frame("iframe1")

# Находим элемент "Your content goes here." и проверяем, что он отображается
content = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//body[text()='Your content goes here.']"))
)
assert content.is_displayed()

# Переключаемся обратно на главный контент
driver.switch_to.default_content()

# Переключаемся на фрейм "Multiple Iframes"
driver.switch_to.frame("iframe2")

# Переключаемся на фрейм "Iframe #1"
driver.switch_to.frame("frame1")

# Находим элемент "Iframe 1" и проверяем, что он отображается
iframe1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Iframe 1']"))
)
assert iframe1.is_displayed()

# Переключаемся обратно на фрейм "Multiple Iframes"
driver.switch_to.parent_frame()

# Переключаемся на фрейм "Iframe #2"
driver.switch_to.frame("frame2")

# Находим элемент "Iframe 2" и проверяем, что он отображается
iframe2 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Iframe 2']"))
)
assert iframe2.is_displayed()

# Переключаемся обратно на главный контент
driver.switch_to.default_content()

# Закрываем браузер
driver.quit()
