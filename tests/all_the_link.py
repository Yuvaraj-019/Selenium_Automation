from SA_ParaBank.utils.driver_factory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = get_driver()
wait = WebDriverWait(driver, 10)

driver.get("https://parabank.parasoft.com")

# Wait for page load
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

# Get all links
links = driver.find_elements(By.TAG_NAME, "a")

unique_links = set()
print("\n=== ALL LINKS FOUND ===")

for link in links:
    href = link.get_attribute("href")
    text = link.text.strip()

    if href and href not in unique_links:
        unique_links.add(href)
        print(f"Text: {text} | URL: {href}")

print("\nTotal unique links found:", len(unique_links))

sleep(2)
driver.quit()
