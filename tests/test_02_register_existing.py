from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

# Click Register link
driver.find_element("link text", "Register").click()
sleep(1.5)

# Fill registration form
driver.find_element("id", "customer.firstName").send_keys("John")
sleep(0.7)
driver.find_element("id", "customer.lastName").send_keys("Cena")
sleep(0.7)
driver.find_element("id", "customer.address.street").send_keys("123 Main Street")
sleep(0.7)
driver.find_element("id", "customer.address.city").send_keys("Mumbai")
sleep(0.7)
driver.find_element("id", "customer.address.state").send_keys("MH")
sleep(0.7)
driver.find_element("id", "customer.address.zipCode").send_keys("400001")
sleep(0.7)
driver.find_element("id", "customer.phoneNumber").send_keys("9876543210")
sleep(0.7)
driver.find_element("id", "customer.ssn").send_keys("778899")
sleep(0.7)

# Login info
driver.find_element("id", "customer.username").send_keys("john99")
sleep(0.7)
driver.find_element("id", "customer.password").send_keys("Password123")
sleep(0.7)
driver.find_element("id", "repeatedPassword").send_keys("Password123")
sleep(1)

# Submit
driver.find_element("xpath", "//input[@value='Register']").click()
sleep(2)

driver.quit()
