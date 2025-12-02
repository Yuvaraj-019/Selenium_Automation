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

driver.find_element("link text", "Request Loan").click()
sleep(2)

driver.find_element("id", "amount").send_keys("2000")
sleep(1)
driver.find_element("id", "downPayment").send_keys("200")
sleep(1)

driver.execute_script("window.scrollBy(0, 200);")
sleep(1)

try:
    account_dropdown = driver.find_element("id", "fromAccountId")
    account_dropdown.click()
    sleep(1)
    driver.find_element("css selector", "#fromAccountId option:nth-child(1)").click()
    sleep(1)
except:
    print("Dropdown not found — but this is normal sometimes.")

driver.find_element("xpath", "//input[@value='Apply Now']").click()
sleep(2)

driver.execute_script("window.scrollBy(0, 300);")
sleep(1.5)

driver.quit()
