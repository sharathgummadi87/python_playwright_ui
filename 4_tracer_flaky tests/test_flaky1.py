from playwright.sync_api import Page, expect

'''
The below tests works fine, but to understand the flaky test behavior
flaky means sometimes pass and sometimes fail
Here as soon as logged in into application I manually clicked contacts,
  to understand flaky behavior with re-runs how it would behave 
   pytest test_flaky1.py --reruns 3 --reruns-delay 2
   
   and refer this :
   file:///C:/Users/shara/Downloads/day32-Screenshots,+Videos,Traceviewer+&+flakytest-1.pdf
'''


def test_Login(page: Page):

    page.goto('https://www.demoblaze.com/index.html')

    login = page.locator("//a[@id='login2' or normalize-space()='Log in']")
    print("clicking:",login.inner_text())
    login.click()
    username = page.locator("//input[@id='loginusername']")
    username.fill("skumar@24")
    password = page.locator("//input[@id='loginpassword']")
    password.fill("skumar@24")
    page.locator("//button[@class='btn' or normalize-space()='Log in']").click()
    page.wait_for_timeout(2000)
    categories = page.locator("//a[@id='cat' or normalize-space()='CATEGORIES']")
    print("verifying:",categories.inner_text())
    expect(categories).to_contain_text("CATEGORIES")
    page.wait_for_timeout(2000)
    categ_list = page.locator("//div[@class='list-group']/a[@id='itemc']")
    count = categ_list.count()
    for item in range(count):
        text = categ_list.nth(item).inner_text()
        print(text)
    page.wait_for_timeout(2000)

    page.locator("//a[@id='logout2' or normalize-space()='Log out']").click()
    print("clicked logout")
    page.wait_for_timeout(2000)
