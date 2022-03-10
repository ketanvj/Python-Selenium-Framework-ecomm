import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.sanity
def test_chrome_headless():
    print(type(webdriver))
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe", options=options)
    print(driver.name)
    driver.maximize_window()

    driver.get("https://nichethyself.com/tourism/home.html")
    driver.find_element(By.NAME, "username").send_keys("stc123")

    driver.find_element(By.NAME, "password").send_keys("12345")
    driver.find_element(By.NAME, "password").submit()
    print("Title is", driver.title)
    driver.quit()