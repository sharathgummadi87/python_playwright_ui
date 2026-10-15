# my_account_page.py
# =====================
# This class represents the "My Account" page of the application.
# It follows the Page Object Model (POM) pattern to separate
# the page locators and actions from the actual test cases.

from playwright.sync_api import Page, expect
from Pages.logout_page import LogoutPage  # Adjust import path based on your project structure


class MyAccountPage:
    """Page Object Model class for the My Account Page."""

    def __init__(self, page):
        '''
            page is an object which is passed while creating an object from testcase file
            self.page = page ==> self.page is instance attribute storing that page object
            self.page instance attribute referring to page object too
            understand when created an object for this class from test file
            myaccount =  MyAccountPage(page)
            Here 'myaccount' is acts or using self.page to navigate or access
                to current class(MyAccountPage) action methods

        '''
        self.page = page

        # ===== Locators =====
        # Identifying elements on the My Account page.

        # ===== Locators =====
        # Identifying elements on the My Account page.
        self.msg_heading = page.locator("//h2[normalize-space()='My Account']")
        self.lnk_logout = page.locator("//div[@class='list-group']/a[normalize-space()='Logout']")

        # ===== Page Validation Methods =====

    def get_page_title(self) -> str:
        """
        Returns the title of the current page.

        Example:
            assert my_account_page.get_page_title() == "My Account"
        """
        try:
            return self.page.title()
        except Exception as e:
            print(f"Error retrieving page title: {e}")
            return ""

    def get_my_account_page_heading(self):

        """
            Returns the locator for the 'My Account' page heading.
            Can be used in test assertions to verify page visibility.

            Example:
            expect(my_account_page.get_my_account_page_heading()).to_be_visible()
        """
        try:
            return self.msg_heading
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None

    # ===== Logout Action =====

    def click_logout(self) -> LogoutPage:

        '''
        Clicks on the 'Logout' link to log out the user.
        Returns an instance of the LogoutPage class
        to allow chained navigation in tests.
        Example:
            logout_page = my_account_page.click_logout()
        For detailed information written below can refer the documentation
        '''
        try:
            self.lnk_logout.click()
            return LogoutPage(self.page)
            raise e  # Re-raise the exception to fail the test intentionally
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise e  # Re-raise the exception to fail the test intentionally








'''
Step 1: First understand return
Imagine you have a function that adds two numbers.

def add_numbers():
    return 10 + 20

result = add_numbers()
print(result)

Output:

30
What happened?

add_numbers() calculates 10 + 20.

return sends the result, 30, back to the place where the function was called.

result receives that value.

Remember: return gives something back to the caller.

Step 2: Now imagine returning an object
Look at this simple example:

class Student:
    pass

def create_student():
    return Student()

student = create_student()

Here:

Student() creates a Student object.

return Student() sends that object back to the caller.

student now refers to that Student object.

So, return can return an object, not just a number or a string.

Step 3: Now connect this to your Playwright code
Your instructor wrote:

def click_logout(self) -> LogoutPage:
    try:
        self.lnk_logout.click()
        return LogoutPage(self.page)
    except Exception as e:
        print(f"Unable to click Logout link: {e}")
        raise e

Focus only on these two lines for now:

self.lnk_logout.click()
return LogoutPage(self.page)

Imagine you are currently working with the MyAccountPage class.

When you call:

logout_page = my_account_page.click_logout()

Python executes the method in this order:

1. Click Logout

self.lnk_logout.click()

2. Create a LogoutPage object

LogoutPage(self.page)

3. Return that object

return LogoutPage(self.page)

4. Store the returned object

logout_page = ...

But buddy, how can one page return another page?
Here's the important correction: it is not returning a different browser tab or browser page. 
It is returning a new Python object of the LogoutPage class.

Look at this line:

return LogoutPage(self.page)

LogoutPage is a Python class.

self.page is the existing Playwright Page object.

LogoutPage(self.page) creates a new LogoutPage object and passes the same browser page to it.

return gives that new object back to the caller.

Both page-object classes can work with the same browser tab.

For example, your LogoutPage class might look like this:

class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.logout_message = page.locator(
            "//h1[normalize-space()='Account Logout']"
        )

Notice that the constructor receives the existing Playwright page object. 
It does not create a new browser tab.

Step 4: Why is this useful in POM?
Suppose you want to click Logout and then verify the logout page.

logout_page = my_account_page.click_logout()
logout_page.verify_logout_message()

The first method returns a LogoutPage object. 
You can then use that object to call methods defined in the LogoutPage class.

One final detail: -> LogoutPage in your instructor's method is a return type hint. 
It tells readers and IDEs that the method is expected to return a LogoutPage object.
 It does not itself perform the return.

The main idea to remember: return LogoutPage(self.page) 
creates and returns a page-object wrapper around the existing browser page, 
so your test can continue using methods from the LogoutPage class.

'''