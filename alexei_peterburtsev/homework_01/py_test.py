''' test webdriver '''

from selenium import webdriver # pylint: disable=E0401

driver = webdriver.Chrome()
driver.get("https://hoster.by")
assert "Example Domain" in driver.title
driver.quit()
