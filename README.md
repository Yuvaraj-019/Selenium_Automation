# Selenium_Automation
Automation Testing of website/Application
Below is a **premium, advanced, GitHub-ready README.md**, fully customized for your **Selenium Automation Framework** with **20+ test cases**, including dropdowns, tables, iFrames, window handling, and full Parabank coverage.

---
My Work: https://youtu.be/Tiu6jPLs8uM?si=8CO-6zGwhvotV8gE


This repository contains a **Python + Selenium automated testing framework** for the **Parabank Demo Application**:

🔗 [https://parabank.parasoft.com](https://parabank.parasoft.com)

It includes **20+ end-to-end test scenarios**, advanced UI interactions, window handling, iFrames, dropdowns, tables, and complete functional test coverage of the application.

---

# 📁 **Project Structure**

```
📦 Parabank-Selenium-Automation
 ┣ 📂 SA_ParaBank
 │   ┗ 📂 utils
 │        ┗ driver_factory.py
 ┣ 📂 tests
 │   ┣ all_the_link.py
 │   ┣ dropdown_handling.py
 │   ┣ max_Min_Screen.py
 │   ┣ TABLE_HANDLING.py
 │   ┣ test_01_register.py
 │   ┣ test_02_register_existing.py
 │   ┣ test_03_login_success.py
 │   ┣ test_04_invalid_login.py
 │   ┣ test_05_forgot_login.py
 │   ┣ test_06_logout.py
 │   ┣ test_07_open_account.py
 │   ┣ test_08_transfer_funds.py
 │   ┣ test_09_bill_payment.py
 │   ┣ test_10_account_overview.py
 │   ┣ test_11_account_activity.py
 │   ┣ test_12_update_profile.py
 │   ┣ test_13_request_loan.py
 │   ┣ test_14_find_transaction_amount.py
 │   ┣ test_15_contact_us.py
 │   ┣ test_16_homepage_links.py
 │   ┣ test_17_location.py
 │   ┣ test_18_services_page.py
 │   ┣ test_19_about_page.py
 │   ┗ test_20_sitemap.py
 ┣ README.md
 ┗ requirements.txt
```

---

# ⭐ **Framework Highlights**

### ✔ **Full Functional Test Coverage**

Covers all major Parabank operations:

* Registration
* Login + Invalid login
* Bill Payment
* Transfer Funds
* Open Account
* Transaction Search
* Account Overview & Activity
* Request Loan
* Profile Update
* Logout

### ✔ **Advanced Selenium Handling**

* Dropdown selection
* Radio buttons
* iFrame switching
* Table extraction
* Multiple link scraping
* Window maximize/minimize/fullscreen
* Web element validations
* Assertions & navigation checks

### ✔ **Reusable Driver Factory**

Centralized `get_driver()` for WebDriver configuration:

```
from SA_ParaBank.utils.driver_factory import get_driver
```

---

# 🌐 **Technologies Used**

| Tool                   | Purpose            |
| ---------------------- | ------------------ |
| **Python 3.x**         | Scripting          |
| **Selenium WebDriver** | Browser Automation |
| **ChromeDriver**       | Chrome Automation  |
| **PyTest (Optional)**  | Test Execution     |
| **Time/Sleep**         | Synchronization    |

---

# 🔥 **Major Features Implemented**

### 🎯 **1. Login & Authentication Tests**

* Valid login
* Invalid login
* Forgot login
* Logout verification

### 🎯 **2. Registration & Existing User Validation**

### 🎯 **3. Account Operations**

* Open new account
* Account overview table extraction
* Account activity search

### 🎯 **4. Fund Operations**

* Transfer funds
* Bill Payment

### 🎯 **5. Loan Request Automation**

### 🎯 **6. Website Navigation Tests**

* Services page
* About page
* Locations page
* Sitemap
* Homepage links extraction
* Extracting ALL links from the website

### 🎯 **7. Form Handling**

* Contact Us form
* Update profile

### 🎯 **8. Element Advanced Handling**

* Dropdown selection
* Table handling
* Window maximize/minimize/fullscreen
* Radio button selection
* iFrame handling (External site because Parabank has no iframe)

---

# 🪟 **Window Handling Example**

```python
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.set_window_size(1024, 768)
```

---

# 🧩 **iFrame Handling Example (External Site)**

Used website: [https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe)

```python
driver.switch_to.frame("iframeResult")

inner = driver.find_element("tag name", "iframe")
driver.switch_to.frame(inner)

print(driver.find_element("tag name", "h1").text)

driver.switch_to.default_content()
```

---

# 📊 **Table Handling Example (Account Table)**

```python
rows = driver.find_elements("xpath", "//table[@id='accountTable']//tr")

for row in rows:
    cols = row.find_elements("tag name", "td")
    print([c.text for c in cols])
```

---

# 📜 **How to Run**

### ✔ Install dependencies

```
pip install -r requirements.txt
```

### ✔ Run a test script

```
python tests/test_03_login_success.py
```

### ✔ Run everything (if PyTest enabled)

```
pytest -v
```

---

# 🧪 **Included Test Cases (20+)**

| Test Case                      | File                               |
| ------------------------------ | ---------------------------------- |
| Register user                  | test_01_register.py                |
| Existing user registration     | test_02_register_existing.py       |
| Valid login                    | test_03_login_success.py           |
| Invalid login                  | test_04_invalid_login.py           |
| Forgot login                   | test_05_forgot_login.py            |
| Logout                         | test_06_logout.py                  |
| Open account                   | test_07_open_account.py            |
| Transfer funds                 | test_08_transfer_funds.py          |
| Bill payment                   | test_09_bill_payment.py            |
| Account overview               | test_10_account_overview.py        |
| Account activity               | test_11_account_activity.py        |
| Update profile                 | test_12_update_profile.py          |
| Request loan                   | test_13_request_loan.py            |
| Transaction search             | test_14_find_transaction_amount.py |
| Contact us                     | test_15_contact_us.py              |
| Homepage links                 | test_16_homepage_links.py          |
| Locations page                 | test_17_location.py                |
| Services page                  | test_18_services_page.py           |
| About page                     | test_19_about_page.py              |
| Sitemap page                   | test_20_sitemap.py                 |
| All websites links extractions | all_the_link.py                    |
| Dropdown handling              | dropdown_handling.py               |
| Table handling                 | TABLE_HANDLING.py                  |
| Max/Min window handling        | max_Min_Screen.py                  |

---


Other Testing :

| **Topic**                        | **Details**                                                      | **Type**                        |
| -------------------------------- | ---------------------------------------------------------------- | ------------------------------- |
| Selenium: Elements & Locators    | Locators: ID, name, class, XPath, CSS                            | Lab                             |
| Browser Extension for Locators   | Tools: SelectorsHub, ChroPath; Demo: XPath for Amazon search box | Demonstration & Hands-On        |
| SelectorsHub Deep Dive           | Advanced XPath & CSS                                             | Lab                             |
| Automate Login Functionality     | Writing login scripts                                            | Lab & Hands-On                  |
| Browser Commands                 | get(), back(), forward(), refresh()                              | Lab & Hands-On                  |
| Viewport in Selenium             | Window size & screenshot                                         | Lab & Hands-On                  |
| Handling Checkboxes              | Selecting / Deselecting                                          | Lab & Hands-On                  |
| Handling Dropdowns               | Select class usage                                               | Lab & Hands-On                  |
| Handling Broken Links / Images   | HTTP status checks using `requests`                              | Lab                             |
| Mid-Term                         | —                                                                | —                               |
| Handling Multiple Tabs / Windows | switch_to.window()                                               | Textbook, References & Hands-On |
| Handling Web Tables              | Extract rows & columns                                           | Textbook, References & Hands-On |
| Handling Iframes                 | switch_to.frame()                                                | Textbook, References & Hands-On |
| Handling Nested Iframes          | Multiple frame switching                                         | Textbook, References & Hands-On |
| Handling JavaScript Alerts       | accept(), dismiss(), send_keys()                                 | Textbook, References & Hands-On |
| Handling Date Picker             | Enter date or select calendar cells                              | Lab & Hands-On                  |
| Handling Dropdown Date Picker    | Navigate using arrows to select dates                            | Lab & Hands-On                  |
| Handling Drag & Drop             | ActionChains                                                     | Lab & Hands-On                  |
| Handling Slider                  | Move slider handle                                               | Lab & Hands-On                  |
| Handling Resizable Elements      | Resize divs using ActionChains                                   | Lab & Hands-On                  |




THANK YOU
