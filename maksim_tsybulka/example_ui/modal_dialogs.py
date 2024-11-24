""""Импорирование библиотек """
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalDialogsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/modal-dialogs")

    def test_modal_dialogs(self):
        driver = self.driver
        buttons = driver.find_elements(By.XPATH, "//div[@class='modal-body']/preceding-sibling::div/button")
        for button in buttons:
            button.click()
            time.sleep(1)
            mod_con = "modal-content"
            modal_dialog = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, mod_con)))
            modal_dialog_title = modal_dialog.find_element(By.CLASS_NAME, "modal-title").text
            expected_modal_dialog_title = button.text
            self.assertEqual(modal_dialog_title, expected_modal_dialog_title)
            modal_dialog.find_element(By.XPATH, "//button[text()='Close']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
