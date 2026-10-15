from playwright.sync_api import Page, expect


def test_launch_browser(page:Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_url("https://www.google.com/")
    expect(page).to_have_title("Google")


def test_orange_page(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Password").fill("admin123")
    page.wait_for_timeout(2000)
    page.get_by_role("button",name='Login').click()
    page.wait_for_timeout(2000)
    expect(page.get_by_role("heading",name='Dashboard')).to_be_visible()
    expect(page.get_by_role("heading", name='Dashboard')).to_have_text("Dashboard")

    page.locator("span.oxd-userdropdown-tab").click()
    page.wait_for_timeout(2000)
    expect(page.locator("//a[normalize-space()='Logout']")).to_be_visible()
    page.locator("//a[normalize-space()='Logout']").click()








