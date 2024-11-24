""""Импорирование библиотек """
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class NestedFramesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/nestedframes")

    def test_nested_frames(self):
        driver = self.driver
        driver.switch_to.frame("frame1")
        driver.switch_to.frame("frame3")
        text = driver.find_element(By.XPATH, "//body[contains(text(),'Sample Nested Frames page')]").text
        expected_text = "Sample Nested Frames page"
        self.assertEqual(text, expected_text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
