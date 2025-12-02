from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

# Login
driver.find_element("name", "username").send_keys("john99")
sleep(1.2)
driver.find_element("name", "password").send_keys("pass123")
sleep(1.2)
driver.find_element("xpath", "//input[@value='Log In']").click()
sleep(2)   # give login page extra time

# Transfer Funds
driver.find_element("link text", "Transfer Funds").click()
sleep(2)   # important wait, page loads slowly

driver.find_element("id", "amount").send_keys("100")
sleep(1.2)

driver.find_element("xpath", "//input[@value='Transfer']").click()
sleep(2)

driver.quit()
