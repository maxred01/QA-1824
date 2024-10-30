from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://hoster.by")
assert "Example Domain" in driver.title
driver.quit()

