""""Импорирование библиотек """
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Запускаем браузер
driver = webdriver.Chrome()

# Переходим на страницу со слайдером
driver.get("https://demoqa.com/slider")

# Ожидаем загрузки страницы
time.sleep(2)

# Находим слайдер на странице
slider = driver.find_element_by_xpath("//div[@id='sliderContainer']/input")

# Вводим значение в поле ввода
slider_input = driver.find_element_by_xpath("//input[@id='sliderValue']")
slider_input.clear()
slider_input.send_keys("70")
slider_input.send_keys(Keys.ENTER)

# Проверяем значение слайдера
assert slider.get_attribute("value") == "70"

# Перемещаем слайдер вправо на 50%
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(50, 0).release().perform()

# Проверяем значение слайдера
assert slider.get_attribute("value") == "100"

# Перемещаем слайдер влево на 25%
action.click_and_hold(slider).move_by_offset(-25, 0).release().perform()

# Проверяем значение слайдера
assert slider.get_attribute("value") == "75"

# Закрываем браузер
driver.quit()
