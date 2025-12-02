from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep
import random

def smart_sleep(min_s=1.2, max_s=2.0):
    sleep(random.uniform(min_s, max_s))

driver = get_driver()
driver.get("https://parabank.parasoft.com")
smart_sleep()

driver.find_element("name", "username").send_keys("john99")
smart_sleep()
driver.find_element("name", "password").send_keys("pass123")
smart_sleep()
driver.find_element("xpath", "//input[@value='Log In']").click()
smart_sleep()

driver.find_element("link text", "Find Transactions").click()
smart_sleep()

amount_box = driver.find_element("id", "criteria.amount")
amount_box.clear()
smart_sleep()
amount_box.send_keys("100")
smart_sleep()

driver.find_element("xpath", "//button[contains(text(),'Find Transactions')]").click()
smart_sleep(2.0, 2.6)

driver.quit()
