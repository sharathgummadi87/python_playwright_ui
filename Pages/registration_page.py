# registration_page.py
from playwright.sync_api import Page


class RegistrationPage:
    """
    Page Object Model class for the Registration Page.
    This class contains web element locators and methods (actions)
    to interact with the registration form.
    """

    def __init__(self, page):
        self.page = page

        # ===== Locators =====
        self.first_name = page.locator("//input[@id='input-firstname']")
        self.last_name = page.locator("//input[@id='input-lastname']")
        self.email = page.locator("//input[@id='input-email']")
        self.telephone = page.locator("//input[@name='telephone']")
        self.password = page.locator("//input[@id='input-password']")
        self.confirm_password = page.locator("//input[@id='input-confirm']")

        # Checkbox and buttons
        self.agree_check_box = page.locator("//input[@name = 'agree']")
        self.continue_button = page.locator("//input[@value = 'Continue']")

        self.msg_confirmation = page.locator("//div[@id='content']/h1[normalize-space()='Your Account Has Been Created!']")

        # ===== Action Methods =====

    def set_first_name(self, firstname):
        """Enter the user's first name into the 'First Name' field."""
        self.first_name.fill(firstname)

    def set_last_name(self, lastname):
        """Enter the user's last name into the 'Last Name' field."""
        self.last_name.fill(lastname)

    def set_email(self, email):
        """Enter the user's email address."""
        self.email.fill(email)

    def set_telephone(self, telephone):
        """Enter the user's telephone number."""
        self.telephone.fill(telephone)

    def set_password(self, password):
        """Enter the password."""
        self.password.fill(password)

    def set_confirm_password(self, confirmpassword):
        """Re-enter the password in the 'Confirm Password' field."""
        self.confirm_password.fill(confirmpassword)

    def set_privacy_policy(self):
        """Select the 'Privacy Policy' checkbox."""
        self.agree_check_box.click()

    def click_continue(self):
        """Click on the 'Continue' button to submit the registration form."""
        self.continue_button.click()

    def get_confirmation_msg(self):
        """
        Return the confirmation message locator.
        This can be used to verify successful registration.
        """
        return self.msg_confirmation









