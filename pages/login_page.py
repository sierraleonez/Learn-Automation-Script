# filename: pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class LoginPage(BasePage):
    _username_input = {"by": By.XPATH, "value": "//input[@id='txt-email']"}
    _password_input = {"by": By.XPATH, "value": "//input[@id='txt-password']"}
    _submit_button = {"by": By.XPATH, "value": "//button[normalize-space()='Sign in']"}
    _logout_session_confirmation = {"by" : By.XPATH, "value" : "//h4[contains(text(),'Logout Session Confirmation!')]"}
    _fail_message = {"by" : By.XPATH, "value" : "//li[contains(text(),'Oops! You have entered the wrong email address or ')]"}
    _submit_logout_button = {"by" : By.XPATH, "value" : "//button[contains(text(),'Continue')]"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("https://learnweb.csc.cxs.cloud/learner/index.html#/discover")

    def with_(self, username, password):
        self._wait_until_displayed(self._username_input)
        self.driver.find_element(self._username_input["by"],
                                 self._username_input["value"]).send_keys(username)
        self.driver.find_element(self._password_input["by"],
                                 self._password_input["value"]).send_keys(password)
        self.driver.find_element(self._submit_button["by"],
                                 self._submit_button["value"]).click()

    def success_message_present(self):
        self._wait_until_displayed(self._logout_session_confirmation)        
        return self.driver.find_element(
            self._logout_session_confirmation["by"], self._logout_session_confirmation["value"]).is_displayed()

    def failure_message_present(self):
        return self.driver.find_element(
            self._fail_message["by"], self._fail_message["value"]).is_displayed()

    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "bad password")
        assert login.failure_message_present()