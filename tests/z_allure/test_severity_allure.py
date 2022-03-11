import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.CRITICAL)
class TestServerity:
    browser = 0

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(driver):
        driver = webdriver.Firefox(executable_path="../resources/geckodriver.exe")
        global browser
        browser = driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://nichethyself.com/tourism/home.html")
        driver.find_element(By.NAME, 'username').send_keys('stc123')
        # driver.find_element_by_name("username").send_keys("stc123")
        driver.find_element(By.NAME, 'password').send_keys('12345')
        # driver.find_element_by_name("password").send_keys("12345")
        status = True
        driver.find_element(By.NAME, 'loginform').submit()

        allure.attach(driver.get_screenshot_as_png(), name="logged_in_user",
                      attachment_type=AttachmentType.PNG)
        if status == True:
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name="logged_in_user",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_WO_Creation(driver):
        global browser
        driver = webdriver.Firefox(executable_path="../resources/geckodriver.exe")
        global browser
        browser = driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://nichethyself.com/tourism/home.html")
        driver.find_element(By.NAME, 'username').send_keys('stc123')
        # driver.find_element_by_name("username").send_keys("stc123")
        driver.find_element(By.NAME, 'password').send_keys('12345')
        # Not submitted the form
        allure.attach(driver.get_screenshot_as_png(), name="logged_in_user",
                      attachment_type=AttachmentType.PNG)
        status = False
        if status == True:
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name="logged_in_user",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_WO_Creation(driver):
        global browser
        time.sleep(3)

    # Severity markers
    # To mark your tests by severity level you can use
    # @allure.severity decorator.
    # It takes a allure.severity_level enum value as an argument.

def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

    @allure.severity(allure.severity_level.NORMAL)
    class TestClassWithNormalSeverity(object):

        def test_inside_the_normal_severity_test_class(self):
            pass

        @allure.severity(allure.severity_level.CRITICAL)
        def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
            pass

    # pytest tests.py --allure-severities normal,critical