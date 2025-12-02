from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

driver.find_element("link text", "Forgot login info?").click()
sleep(1.5)

driver.find_element("id", "firstName").send_keys("John")
sleep(0.8)
driver.find_element("id", "lastName").send_keys("Doe")
sleep(0.8)
driver.find_element("id", "address.street").send_keys("Street 1")
sleep(0.8)
driver.find_element("id", "address.city").send_keys("Delhi")
sleep(0.8)
driver.find_element("id", "address.state").send_keys("DL")
sleep(0.8)
driver.find_element("id", "address.zipCode").send_keys("110001")
sleep(0.8)


driver.find_element("id", "ssn").send_keys("1234")
sleep(1)


driver.find_element("xpath", "//input[@value='Find My Login Info']").click()
sleep(2)

driver.quit()
