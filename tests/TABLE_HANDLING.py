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
sleep(1.5)

driver.find_element("link text", "Accounts Overview").click()
sleep(1.5)

rows = driver.find_elements("css selector", "#accountTable tbody tr")
print(f"Total Rows Found: {len(rows)}")

for r in rows:
    cols = r.find_elements("tag name", "td")
    data = [c.text for c in cols]
    print(data)
    sleep(0.5)

sleep(2)
driver.quit()
