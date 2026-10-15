from playwright.sync_api import sync_playwright, expect, Page, Playwright


# Browser--> context---> page/s
# Browser -> context(user profile) -> page(window or tab)

def test_browsercontext(playwright:Playwright):
    # chromium=playwright.chromium
    # browser=chromium.launch()

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()  # created page1
    page2 = context.new_page()  # created page2

    page1.goto("https://playwright.dev/")
    print("The title:", page1.title())
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    page1.wait_for_timeout(2000)

    page2.goto("https://www.selenium.dev/")
    print("The title:", page2.title())
    expect(page2).to_have_title("Selenium")
    page2.wait_for_timeout(2000)

