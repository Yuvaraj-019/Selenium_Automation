from SA_ParaBank.utils.driver_factory import get_driver
from time import sleep

driver = get_driver()
driver.get("https://parabank.parasoft.com")
sleep(2)

driver.set_window_size(1500, 1000)
print("Window minimized")
sleep(2)

driver.maximize_window()
print("Window maximized")
sleep(2)



driver.set_window_position(-2000, 0)
print("Window moved off-screen")
sleep(2)

driver.quit()
