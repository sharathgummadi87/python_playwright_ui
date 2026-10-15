from playwright.sync_api import Page, expect

from Login_Page import LoginPage
from Home_Page import HomePage
from Cart_Page import CartPage

import pytest



@pytest.mark.parametrize("username, password, product_name", [('skumar@24', 'skumar@24','Samsung galaxy s6')])
def test_add_product_cart(page:Page, username, password, product_name):

    page.goto("https://www.demoblaze.com/index.html")

    # calling LoginPage action methods
    login_page = LoginPage(page)   #created object for the LoginPage class

    login_page.click_login_link()
    login_page.enter_username(username)
    page.wait_for_timeout(2000)
    login_page.enter_password(password)
    page.wait_for_timeout(2000)
    login_page.click_login_button()
    page.wait_for_load_state()

    # calling HomePage action methods
    home_page = HomePage(page)  #created object for the HomePage class

    home_page.get_all_product()
    page.wait_for_timeout(2000)
    home_page.add_product(product_name)
    page.wait_for_load_state()
    home_page.click_cart()
    page.wait_for_load_state()



    # calling CartPage action methods
    cart_page = CartPage(page)
    product_text = cart_page.verify_product_name(product_name)
    expect(product_text).to_be_visible()
    # expect(product_text).to_equal('Samsung galaxy s6')















