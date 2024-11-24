""""Импорирование библиотек """
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoQaFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/automation-practice-form")

    def test_fill_form(self):
        driver = self.driver

        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")

        driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]').click()

        driver.find_element(By.ID, "userNumber").send_keys("1234567890")
        driver.find_element(By.ID, "dateOfBirthInput").send_keys("01 Jan 1990")
        driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.ENTER)

        driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
        driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
        driver.find_element(By.ID, "subjectsInput").send_keys("English")
        driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)

        driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()
        driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, New York")

        state_dropdown = driver.find_element(By.ID, "state")
        state_dropdown.click()
        state_option = driver.find_element(By.XPATH, '//div[contains(@class, "menu")]/div[contains(text(), "NCR")]')
        state_option.click()

        city_dropdown = driver.find_element(By.ID, "city")
        city_dropdown.click()
        city_option = driver.find_element(By.XPATH, '//div[contains(@class, "menu")]/div[contains(text(), "Delhi")]')
        city_option.click()

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))

        result_name = driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[2]').text
        self.assertEqual(f"{'John'} {'Doe'}", result_name)

        result_email = driver.find_element(By.XPATH, '//table/tbody/tr[2]/td[2]').text
        self.assertEqual("johndoe@example.com", result_email)

        result_phone = driver.find_element(By.XPATH, '//table/tbody/tr[4]/td[2]').text
        self.assertEqual("1234567890", result_phone)

        result_address = driver.find_element(By.XPATH, '//table/tbody/tr[6]/td[2]').text
        self.assertEqual("123 Main Street, New York", result_address)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
