""""Импорирование библиотек """
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestDemoQA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/menu#")

    def test_menu(self):
        driver = self.driver
        menu_items = driver.find_elements_by_css_selector(".menu-list li")

        for item in menu_items:
            ActionChains(driver).move_to_element(item).perform()
            sub_menu = item.find_elements_by_css_selector(".submenu-list li")

            for sub_item in sub_menu:
                ActionChains(driver).move_to_element(sub_item).perform()
                time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
