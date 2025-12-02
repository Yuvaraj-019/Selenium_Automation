from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep
from selenium.webdriver.common.by import By
import random

def smart_sleep(a=0.9, b=1.7):
    sleep(random.uniform(a, b))

driver = get_driver()
driver.get("https://parabank.parasoft.com")
smart_sleep()

about = driver.find_element(By.LINK_TEXT, "About Us")
about.click()
smart_sleep()

driver.execute_script("window.scrollTo(0, 500)")
smart_sleep()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
smart_sleep()

services = driver.find_element(By.LINK_TEXT, "Services")
services.click()
smart_sleep()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
smart_sleep()

products = driver.find_element(By.LINK_TEXT, "Products")
products.click()
smart_sleep()
driver.execute_script("window.scrollTo(0, 600)")
smart_sleep()

locations = driver.find_element(By.LINK_TEXT, "Locations")
locations.click()
smart_sleep()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
smart_sleep()

try:
    admin = driver.find_element(By.LINK_TEXT, "Admin Page")
    admin.click()
    smart_sleep()
except:
    print("Admin Page not visible — skipping.")


home = driver.find_element(By.LINK_TEXT, "home")
home.click()
smart_sleep()

driver.quit()
