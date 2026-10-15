from playwright.sync_api import Page, expect
from Pages.login_page import LoginPage


import time
import pytest
from playwright.sync_api import expect
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.my_account_page import MyAccountPage
from config import Config  # Configuration file holding credentials


def test_valid_user_login(page):
    """
    Automated Test Case: Verify that login succeeds for valid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # page.goto("http://localhost/opencart/upload/index.php?route=account/login")

    home_page.click_home_my_account()
    page.wait_for_timeout(2000)
    home_page.click_login_link()
    page.wait_for_timeout(2000)

    login_page.enter_email_id(Config.email)
    page.wait_for_timeout(2000)
    login_page.enter_email_password(Config.password)
    page.wait_for_timeout(2000)
    login_page.click_login_button()
    page.wait_for_timeout(2000)

    # Wait for the page to load completely after login
    time.sleep(3)
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)


def test_invalid_user_login(page):
    """
    Automated Test Case: Verify that login succeeds for valid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    #page.goto("http://localhost/opencart/upload/index.php?route=account/login")

    home_page.click_home_my_account()
    page.wait_for_timeout(2000)
    home_page.click_login_link()
    page.wait_for_timeout(2000)

    login_page.enter_email_id(Config.invalid_email)
    page.wait_for_timeout(2000)
    login_page.enter_email_password(Config.invalid_password)
    page.wait_for_timeout(2000)
    login_page.click_login_button()
    page.wait_for_timeout(2000)

    # Wait for the page to load completely after login
    time.sleep(3)
    expect(login_page.get_login_error()).to_be_visible(timeout=3000)












# def test_login_opencart(page:Page):
#     page.goto("http://localhost/opencart/upload/index.php?route=account/login")
#     login = LoginPage(page)
#
#     try:
#         print("Step 1: Starting login")
#         login.enter_email_id("kumarsharath1720@gmail.com")
#         print("Entered email ID")
#         page.wait_for_timeout(1000)
#         login.enter_email_password("admin")
#         print("Entered email password")
#         page.wait_for_timeout(1000)
#         login.click_login_button()
#         print("Click login button")
#         page.wait_for_timeout(1000)
#         print("Step 2: Checking Account information")
#         expect(page.locator("//a[normalize-space()='Edit your account information']")).to_be_visible()
#         print("Step 3: Search box is visible")
#     except Exception as e:
#         print("\n ====> EXCEPT BLOCK EXECUTED")
#         error_msg = login.get_login_error()
#         # error_text = error_msg.inner_text()
#         print("error message:", error_msg.inner_text())
#         raise
#





