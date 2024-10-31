from selenium import webdriver

# Укажите путь к ChromeDriver (если не добавлен в PATH)
driver = webdriver.Chrome()  # Если добавлен в PATH, просто используйте webdriver.Chrome()

# Откройте страницу
driver.get("https://hoster.by")

# Проверка заголовка страницы
# assert "Example Domain" in driver.title

# Закрыть браузер
driver.quit()