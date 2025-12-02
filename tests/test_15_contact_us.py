from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep
import random

def smart_sleep(min_s=1.2, max_s=2.0):
    sleep(random.uniform(min_s, max_s))

driver = get_driver()
driver.get("https://parabank.parasoft.com")
smart_sleep()

driver.find_element("link text", "Contact Us").click()
smart_sleep()

name_field = driver.find_element("id", "name")
name_field.clear()
smart_sleep()
name_field.send_keys("John")
smart_sleep()

email_field = driver.find_element("id", "email")
email_field.clear()
smart_sleep()
email_field.send_keys("test@mail.com")
smart_sleep()

subject_field = driver.find_element("id", "subject")
subject_field.clear()
smart_sleep()
subject_field.send_keys("Testing")
smart_sleep()

comment_field = driver.find_element("id", "comment")
comment_field.clear()
smart_sleep()
comment_field.send_keys("Test message")
smart_sleep()

driver.find_element("xpath", "//input[@value='Send to Customer Care']").click()
smart_sleep(2.0, 2.5)

driver.quit()
