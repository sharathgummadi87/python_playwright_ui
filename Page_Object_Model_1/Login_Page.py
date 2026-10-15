from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page:Page):

        self.page = page
        self.login_link = page.locator("//a[@id='login2']")
        self.user_name_input = page.locator("//input[@id='loginusername']")
        self.password_input = page.locator("//input[@id='loginpassword']")
        self.login_button = page.locator("//button[normalize-space()='Log in']")


    def click_login_link(self):
        self.login_link.click()
        print("Login link is clicked")

    def enter_username(self,username):
        self.user_name_input.fill(username)
        print("Username entered")

    def enter_password(self, password):
        self.password_input.fill("")
        self.password_input.fill(password)
        print("Password entered")


    def click_login_button(self):
        self.login_button.click()
        print("Login button is clicked")



















