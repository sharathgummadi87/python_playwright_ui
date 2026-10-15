from playwright.sync_api import sync_playwright, expect, Playwright

def test_browser_popups(playwright:Playwright):

    # browser -> context(user profile) -> page(window or tab)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    # registering ana event to handle browser popups
    page.on("popup", lambda popup:popup.wait_for_load_state())

    page.locator("//button[@id='PopUp']").click()

    page.wait_for_timeout(5000)
    all_pages = context.pages
    print("No of child web-pages or windows or Tabs:", len(all_pages))
    page.wait_for_timeout(5000)

    for pagee in all_pages:
        title = pagee.title()
        print("The title is:", title)
        if 'Selenium' in title:
            pagee.locator("//a[normalize-space()='Documentation']").click()
            print("Documentation is clicked")
            pagee.wait_for_timeout(3000)
            selenium_manager = pagee.locator("//ul[@class='ul-1']//a[@id='m-documentationselenium_manager']")
            expect(selenium_manager).to_be_visible()
    page.wait_for_timeout(3000)








