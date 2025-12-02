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
sleep(2)

# Open Bill Pay
driver.find_element("link text", "Bill Pay").click()
sleep(2)   # important wait because Bill Pay loads slowly

# Fill Bill Payment Form
driver.find_element("id", "payee.name").send_keys("XYZ Corp")
sleep(1)
driver.find_element("id", "payee.address.street").send_keys("Street 2")
sleep(1)
driver.find_element("id", "payee.address.city").send_keys("Mumbai")
sleep(1)
driver.find_element("id", "payee.address.state").send_keys("MH")
sleep(1)
driver.find_element("id", "payee.address.zipCode").send_keys("400001")
sleep(1)
driver.find_element("id", "payee.phoneNumber").send_keys("9090909090")
sleep(1)
driver.find_element("id", "payee.accountNumber").send_keys("1111")
sleep(1)
driver.find_element("id", "verifyAccount").send_keys("1111")
sleep(1)
driver.find_element("id", "amount").send_keys("500")
sleep(1)

# Submit Payment
driver.find_element("xpath", "//input[@value='Send Payment']").click()
sleep(2)

driver.quit()
