# login_page.py
# =====================
# This class represents the "Login Page" of the application.
# It is designed using the Page Object Model (POM) pattern,
# which helps to keep locators and actions separate from the test logic.

from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.email_id = page.locator("//input[@id='input-email']")
        self.email_password = page.locator("//input[@id='input-password']")
        self.login_button = page.locator("//input[@value='Login']")
        self.error_msg = page.locator("//div[contains(@class,'alert')]")

    # ===== Action Methods =====
    # These methods represent user interactions on the Login Page.

    def enter_email_id(self, email_id):
        """Enter the email address in the Email field."""
        try:
            self.email_id.fill(email_id)
        except Exception as e:
            print(f"Error occurred while entering email id :{e}")
            raise

    def enter_email_password(self, email_pwd):
        """Enter the password in the Password field."""
        try:
            self.email_password.fill(email_pwd)
        except Exception as e:
            print(f"Error occurred while entering email password :{e}")
            raise

    def click_login_button(self):
        """Click the Login button."""
        try:
            self.login_button.click()
        except Exception as e:
            print(f"Error occurred while clicking login button :{e}")
            raise

    def get_login_error(self):
        """
            Return the error message element if login fails.
            Example use:
            error_text = login_page.get_login_error().inner_text()
        """
        try:
            return self.error_msg
        except Exception as e:
            print(f"Error occurred while getting login error message :{e}")
            raise


