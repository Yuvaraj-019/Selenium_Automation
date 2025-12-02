import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    # Absolute path to chromedriver
    driver_path = "/home/atreus/PycharmProjects/software_testing/SA_ParaBank/drivers/chromedriver"

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
