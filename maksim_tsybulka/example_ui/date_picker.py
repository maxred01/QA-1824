""""Импорирование библиотек """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация браузера
driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")

# Ожидание загрузки страницы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-group")))

# Получаем поле ввода даты
date_input = driver.find_element(By.CSS_SELECTOR, "#datePickerMonthYearInput")

# Очищаем поле ввода
date_input.clear()

# Вводим новую дату
date_input.send_keys("06/16/2023")

# Ожидаем отображения выбранной даты
DATE_LOC = "#datePickerMonthYearInput"
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, DATE_LOC), "06/16/2023"))

# Получаем все кнопки изменения даты
date_buttons = driver.find_elements(By.CSS_SELECTOR, ".react-datepicker__navigation")

# Изменяем месяц и год на следующий
date_buttons[1].click()
date_buttons[0].click()

# Ожидаем отображения выбранной даты
DATE_PIC = "#datePickerMonthYearInput"
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, DATE_PIC), "07/16/2022"))

# Закрываем браузер
driver.quit()
