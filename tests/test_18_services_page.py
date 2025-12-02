from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep
from selenium.webdriver.common.by import By

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

# Login
driver.find_element(By.NAME, "username").send_keys("john99")
sleep(1)
driver.find_element(By.NAME, "password").send_keys("pass123")
sleep(1)
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
sleep(2)

# Services Page
driver.find_element(By.LINK_TEXT, "Services").click()
sleep(2)

# Scroll down and up
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
driver.execute_script("window.scrollTo(0, 0);")
sleep(1)

# Print links on Services page
services_links = driver.find_elements(By.TAG_NAME, "a")
print("\nLinks on Services page:")
for link in services_links:
    print(link.get_attribute("href"))

# Go back
driver.back()
sleep(2)

# Logout
driver.find_element(By.LINK_TEXT, "Log Out").click()
sleep(2)

driver.quit()
