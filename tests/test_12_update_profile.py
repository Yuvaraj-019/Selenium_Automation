from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

driver.find_element("name", "username").send_keys("john99")
sleep(1)
driver.find_element("name", "password").send_keys("pass123")
sleep(1)
driver.find_element("xpath", "//input[@value='Log In']").click()
sleep(2)

driver.find_element("link text", "Update Contact Info").click()
sleep(2)

driver.find_element("id", "customer.address.city").clear()
sleep(1)
driver.find_element("id", "customer.address.city").send_keys("Chennai")
sleep(1)

driver.find_element("id", "customer.address.state").clear()
sleep(1)
driver.find_element("id", "customer.address.state").send_keys("TN")
sleep(1)

driver.find_element("id", "customer.phoneNumber").clear()
sleep(1)
driver.find_element("id", "customer.phoneNumber").send_keys("8888888888")
sleep(1)

driver.execute_script("window.scrollBy(0, 200);")
sleep(1)

driver.find_element("xpath", "//input[@value='Update Profile']").click()
sleep(2)

driver.execute_script("window.scrollBy(0, 300);")
sleep(1.5)

driver.quit()
