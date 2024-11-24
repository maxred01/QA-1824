""""Импорирование библиотек """
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAccordian(unittest.TestCase):
    def setUp(self):
        # Инициализация браузера
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/accordian")

    def test_accordian(self):
        # Получаем все элементы accordian
        accordians = self.driver.find_elements(By.CSS_SELECTOR, ".accordion > div")

        # Проверяем, что количество accordian равно 3
        self.assertEqual(len(accordians), 3)

        # Разворачиваем каждый accordian и проверяем текст внутри
        for accordian in accordians:
            # Нажимаем на заголовок accordian, чтобы развернуть его
            accordian_header = accordian.find_element(By.CSS_SELECTOR, ".accordion-header")
            accordian_header.click()

            # Ждем, пока текст внутри accordian станет видимым
            accordian_content = accordian.find_element(By.CSS_SELECTOR, ".accordion-body")
            WebDriverWait(self.driver, 5).until(EC.visibility_of(accordian_content))

            # Проверяем, что текст внутри accordian соответствует ожидаемому
            expected_text = accordian.find_element(By.CSS_SELECTOR, ".accordion-body p").text
            actual_text = accordian_content.find_element(By.CSS_SELECTOR, "p").text
            self.assertEqual(expected_text, actual_text)

    def tearDown(self):
        # Закрываем браузер
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
