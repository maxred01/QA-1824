""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Открытие страницы
driver.get("https://demoqa.com/links")

# Ожидание загрузки страницы
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "simpleLink")))

# Нахождение ссылок на странице
home_link = driver.find_element_by_link_text("Home")
created_link = driver.find_element_by_link_text("Created")
no_content_link = driver.find_element_by_link_text("No Content")
moved_link = driver.find_element_by_link_text("Moved")
bad_request_link = driver.find_element_by_link_text("Bad Request")
unauthorized_link = driver.find_element_by_link_text("Unauthorized")
forbidden_link = driver.find_element_by_link_text("Forbidden")
not_found_link = driver.find_element_by_link_text("Not Found")
internal_server_error_link = driver.find_element_by_link_text("Internal Server Error")
service_unavailable_link = driver.find_element_by_link_text("Service Unavailable")
not_implemented_link = driver.find_element_by_link_text("Not Implemented")
broken_link = driver.find_element_by_id("broken-link")

# Проверка каждой ссылки на наличие ошибок
for link in [home_link,
             created_link,
             no_content_link,
             moved_link,
             bad_request_link,
             unauthorized_link,
             forbidden_link,
             not_found_link,
             internal_server_error_link,
             service_unavailable_link,
             not_implemented_link,
             broken_link]:
    link.click()
    if "Error" in driver.title:
        print(f"Ссылка {link.text} содержит ошибку!")
    driver.back()

# Закрытие браузера
driver.quit()
