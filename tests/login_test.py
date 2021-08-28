# filename: tests/login_test.py
import pytest
import os
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def login(request):
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)

    else:
        driver_ = webdriver.Chrome()

    loginPage = LoginPage(driver_)
    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return loginPage

def test_valid_credentials(login):
    login.with_("refactory.44@yopmail.com", "ABCDE1234567890")
    assert login.success_message_present()
    print("success")

def test_invalid_credentials(login):
    login.with_("refactory44@yopmail.com", "ABCDE123456789")
    assert login.failure_message_present()