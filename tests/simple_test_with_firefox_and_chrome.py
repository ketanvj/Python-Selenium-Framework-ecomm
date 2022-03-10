# pip install -U selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.sanity
def test_chrome_headless():
    driver = webdriver.Firefox(executable_path="../../resources/geckodriver.exe")
    driver.maximize_window()
    driver.get("https://nichethyself.com/tourism/home.html")
    ele = driver.find_element(By.NAME, 'username' )
    user = driver.find_element(By.NAME, 'username' )
    user.send_keys('stc123')
    driver.refresh()
    user.send_keys('stc123')
    driver.find_element(By.NAME, 'password' ).send_keys('12345')
    driver.find_element(By.NAME, 'loginform' ).submit()
    print(driver.title)
    assert driver.title == "My account1"
    driver.quit()