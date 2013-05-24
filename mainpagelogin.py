from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://enterprise.readdle.com/")
    wd.find_element_by_id("show_nav").click()
    wd.find_element_by_id("login_value").click()
    wd.find_element_by_id("login_value").clear()
    wd.find_element_by_id("login_value").send_keys("readdle")
    wd.find_element_by_id("pass_value").click()
    wd.find_element_by_id("pass_value").clear()
    wd.find_element_by_id("pass_value").send_keys("glokayakuzdra")
    wd.find_element_by_id("submit").click()
    if not (len(wd.find_elements_by_link_text("Sign Out")) != 0):
        success = False
        print("verifyElementPresent failed")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
