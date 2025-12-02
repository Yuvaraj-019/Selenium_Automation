from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(1.5)

driver.find_element("link text", "Site Map").click()
sleep(2)
driver.quit()
