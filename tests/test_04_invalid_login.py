from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

driver.find_element("name", "username").send_keys("wronguser")
sleep(1.5)
driver.find_element("name", "password").send_keys("wrongpass")
sleep(1.5)
driver.find_element("xpath", "//input[@value='Log In']").click()
sleep(2)

driver.quit()
