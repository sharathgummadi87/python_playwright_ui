from playwright.sync_api import Page

class HomePage:
    """Page Object Model class for the 'Home' page."""

    def __init__(self, page):
        """
         Constructor to initialize the Playwright page object
         and define all necessary locators.
        """
        self.page = page

        # ===== Locators =====
        self.lnk_my_account = page.locator("//span[normalize-space()='My Account']")
        self.hover_my_account = page.locator("//ul[contains(@class,'dropdown-menu')]/li/a[normalize-space()='My Account']")
        self.lnk_register = page.locator(" //li/a[normalize-space()='Register']")
        self.lnk_login = page.locator(" //a[normalize-space()='Login']")
        self.search_box = page.locator("//input[@name='search']")
        self.search_button = page.locator("//span[@class='input-group-btn']/button[@type='button']")

        # ===== Action Methods =====
        # Each method represents a user interaction on the page

    def get_home_page_title(self):
        try:
            title = self.page.title()
            return title
        except Exception as e:
            print(f"Getting error while fetching page title: {e}")
            raise

    def click_home_my_account(self):
        try:
            self.lnk_my_account.click()
        except Exception as e:
            print(f"Exception while clicking 'My Account': {e}")
            raise


    def click_my_account(self):
        try:
            self.hover_my_account.click()
        except Exception as e:
            print(f"Exception while clicking 'Hover My Account': {e}")
            raise

    def click_register(self):
        try:
            self.lnk_register.click()
        except Exception as e:
            print(f"Exception while clicking 'register': {e}")
            raise

    def click_login_link(self):
        try:
            self.lnk_login.click()
        except Exception as e:
            print(f"Exception while clicking 'Login link': {e}")
            raise

    def enter_search_box(self, product_name):
        try:
            self.search_box.fill(product_name)
        except Exception as e:
            print(f"Exception while entering 'search box': {e}")
            raise

    def click_search_button(self):
        try:
            self.search_button.click()
        except Exception as e:
            print(f"Exception while clicking 'search box': {e}")
            raise
