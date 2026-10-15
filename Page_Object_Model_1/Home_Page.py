from playwright.sync_api import Page

'''
Please refer below notes to understand what is class, object, page-fixture, and what is self.page = page
what does self refers to 
'''
class HomePage:

    def __init__(self, page:Page):

        self.page = page
        self.total_products = page.locator("//div[@id='tbodyid']/div")
        self.cart_product_name = page.locator("//a[normalize-space()='Add to cart']")
        self.click_cart_link = page.locator(" //li[@class='nav-item']/a[normalize-space()='Add to cart' or normalize-space()='Cart']")


    def get_all_product(self):

        print("The total_products count is:", self.total_products.count())


    def add_product(self,product_name):

        product = self.page.locator(f"//div[@class='card-block']//a[normalize-space()='{product_name}']")
        product.click()

        print("Selected product:", product_name)

        self.page.on("dialog", lambda dialog:dialog.accept())
        self.cart_product_name.click()
        print("Handled dialoge properly")
        print("Added product")

    def click_cart(self):
        self.click_cart_link.click()

        print("Cart link is clicked")


'''
File 1: Home_Page.py

class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator(
            "//input[@id='small-searchterms']"
        )

    def search_product(self, product_name):
        self.search_box.fill(product_name)
        

File 2: test_home_page.py

from Home_Page import HomePage

def test_search(page):
    home = HomePage(page)
    home.search_product("Laptop")



The flow is:
1. Pytest provides the page fixture.
2. HomePage(page) creates a HomePage object.
3. self.page = page stores the Playwright page reference.
4. self.search_box stores the search-box locator.
5. home.search_product("Laptop") calls the method and fills the search box.
This is the basic idea of the Page Object Model (POM):
keep page-related locators and actions in a page class, and keep test execution in the test file.

Your understanding — corrected
1. page is a fixture provided by pytest-playwright. ✅
Correct! More precisely, page is a pytest fixture that provides a Playwright Page object,
   representing a browser tab or page.
2. home = HomePage(page) ✅
Correct!
- HomePage(page) creates an object of the HomePage class.
- page is the Playwright Page object passed to the class.
- home is the variable that refers to the newly created HomePage object.
3. Is self.page a variable or an attribute?
The best term to use is instance attribute.
self.page = page



- self refers to the current HomePage object.
- page on the right side is the argument received by __init__().
- self.page on the left side is the instance attribute 
   that stores a reference to that Playwright Page object.
You can call it an attribute in your interviews.
 Technically, attributes are also accessed like variables, 
but instance attribute is the more precise term here.
4. self.page refers to the Playwright Page object. ✅
Correct! It lets your class interact with the browser tab,
 for example, by navigating to a website using self.page.goto().
5. The home object can use self.page and the class methods. ✅
Correct! When you call:
home.search_product("Laptop")



Python calls the search_product() method on the home object. 
Inside that method, self refers to home, so self.search_box accesses the locator stored on that object.
Your final mental picture
page fixture
Provides the Playwright Page object

home = HomePage(page)
Creates a HomePage object and passes the page into it

self.page
Stores the Page object


self.search_box
Stores the search-box locator



home.search_product("Laptop")
Uses the stored locator to fill the search box

'''








