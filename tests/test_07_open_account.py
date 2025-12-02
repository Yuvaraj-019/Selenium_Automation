from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

# Login
driver.find_element("name", "username").send_keys("john99")
sleep(1)
driver.find_element("name", "password").send_keys("pass123")
sleep(1)
driver.find_element("xpath", "//input[@value='Log In']").click()
sleep(1.5)

# Open New Account
driver.find_element("link text", "Open New Account").click()
sleep(1.5)

# Click the Open New Account button
driver.find_element("xpath", "//input[@value='Open New Account']").click()
sleep(2)

driver.quit()
