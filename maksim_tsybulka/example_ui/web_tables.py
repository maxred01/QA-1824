""""Импорирование библиотек """
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()

# Переход на страницу с таблицей
driver.get("https://demoqa.com/webtables")

# Находим все строки таблицы
rows = driver.find_elements(By.XPATH, "//table[@id='tableWrapper']/tbody/tr")

# Создаем пустой список для хранения данных из таблицы
table_data = []

# Проходимся по каждой строке таблицы
for row in rows:
    # Находим все ячейки в текущей строке
    cells = row.find_elements(By.TAG_NAME, "td")

    # Создаем пустой список для хранения данных из текущей строки
    row_data = []

    # Проходимся по каждой ячейке в текущей строке
    for cell in cells:
        # Получаем текст из ячейки и добавляем его в список данных текущей строки
        row_data.append(cell.text)

    # Добавляем список данных текущей строки в список данных таблицы
    table_data.append(row_data)

# Выводим данные таблицы в консоль
print(table_data)

# Находим первое поле в таблице и кликаем на него
first_field = driver.find_element(By.XPATH, "//table[@id='tableWrapper']/tbody/tr[1]/td[1]")
first_field.click()

# Очищаем значение поля
first_field.clear()

# Вводим новое значение в поле
first_field.send_keys("New Value")

# Нажимаем клавишу Enter, чтобы сохранить изменения
first_field.send_keys(Keys.ENTER)

# Ждем 1 секунду, чтобы изменения сохранились
time.sleep(1)

# Находим кнопку "Delete" для первой строки в таблице
delete_button = driver.find_element(By.XPATH, "//table[@id='tableWrapper']/tbody/tr[1]/td[11]/span[2]/button")

# Кликаем на кнопку "Delete"
delete_button.click()

# Ждем 1 секунду, чтобы удаление завершилось
time.sleep(1)

# Проходимся по каждой строке в таблице
for i in range(len(rows)):
    # Находим первое поле в текущей строке и кликаем на него
    field = driver.find_element(By.XPATH, f"//table[@id='tableWrapper']/tbody/tr[{i+1}]/td[1]")
    field.click()

    # Очищаем значение поля
    field.clear()

    # Вводим новое значение в поле
    field.send_keys(f"New Value {i+1}")

    # Нажимаем клавишу Enter, чтобы сохранить изменения
    field.send_keys(Keys.ENTER)

    # Ждем 1 секунду, чтобы изменения сохранились
    time.sleep(1)

    # Находим кнопку "Delete" для текущей строки в таблице
    delete_button = driver.find_element(By.XPATH, f"//table[@id='tableWrapper']/tbody/tr[{i+1}]/td[11]/span[2]/button")

    # Кликаем на кнопку "Delete"
    delete_button.click()

    # Ждем 1 секунду, чтобы удаление завершилось
    time.sleep(1)

# Закрываем браузер
driver.quit()
