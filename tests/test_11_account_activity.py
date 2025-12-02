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
sleep(2)

# Go to Accounts Overview
driver.find_element("link text", "Accounts Overview").click()
sleep(1.5)

# Open first account link
driver.find_element("css selector", "table tbody tr td a").click()
sleep(2)

# Now on Account Activity page
# Select date range
driver.find_element("id", "month").send_keys("January")
sleep(1)
driver.find_element("id", "transactionType").send_keys("All")
sleep(1)

# Click Go
driver.find_element("xpath", "//input[@value='Go']").click()
sleep(2)

# Scroll down to view transactions
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1.5)

# Scroll up again
driver.execute_script("window.scrollTo(0, 0);")
sleep(1.5)

# Go back to Accounts Overview
driver.find_element("link text", "Accounts Overview").click()
sleep(1.5)

driver.quit()
