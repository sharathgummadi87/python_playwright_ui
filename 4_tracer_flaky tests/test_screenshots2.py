from playwright.sync_api import sync_playwright, expect, Page
import time
import datetime

'''
we created pytest.ini file which has addopts which handles automatcially 
[pytest]

addopts = --headed
          --browser=chromium
          --video=on
          --screenshot=on
          --tracing=on
to launch browser in --headed and browser is chrome and video & screenshot = on and tracing = on  
this is just to refer I created 
'''

def test_screenshots_demo(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #timestamp=str(int(time.time()))
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")


    # Page screenshot (partially/visible)
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    # Full page screenshot
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)


    # Element/specific section of the page screenshot
    logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshots/logo_{timestamp}.png")

    # specific section
    featuredproducts=page.locator(".product-grid.home-page-product-grid")
    featuredproducts.screenshot(path=f"screenshots/featuredproducts_{timestamp}.png")
