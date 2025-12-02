from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep
from selenium.webdriver.support.ui import Select

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

# Open New Account (has dropdown)
driver.find_element("link text", "Open New Account").click()
sleep(1.5)

# Select Account Type dropdown
account_type = Select(driver.find_element("id", "type"))
account_type.select_by_visible_text("SAVINGS")
sleep(1.2)

# Select From Account dropdown
from_account = Select(driver.find_element("id", "fromAccountId"))
from_account.select_by_index(0)
sleep(1.2)

# Submit
driver.find_element("xpath", "//input[@value='Open New Account']").click()
sleep(2)

driver.quit()
