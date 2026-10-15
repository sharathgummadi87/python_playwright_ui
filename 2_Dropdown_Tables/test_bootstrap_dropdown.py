import pytest
from playwright.sync_api import sync_playwright, expect, Page


''''
Difference between  [.// ] and [ // ] means "search anywhere"

[.// ] --> search inside the current node
[ // ] --> search anywhere from the current node
HTML:

<div class="user">
    <label>Username</label>
    <input type="text">
</div>

<div class="user">
    <label>Password</label>
    <input type="password">
</div>

Q. find the Username write xpath for this one 

I will use .// beacuse I want to find in the current node will go 
.// from the current node/context it will look inside 

//div[@class='user'][.//label[normalize-space()='Username']]

"Search only insdie the current node/context."


//label

Meaning:
Find the <label> anywhere in the page.
So // is basically:

"Search anywhere from the current context."
'''

def test_bootstrapdropdown(page : Page):
    # Launch the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("input[name='username']").fill("admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("//button[normalize-space()='Login']").click()
    page.wait_for_timeout(2000)
    expect(page.locator("//h6[normalize-space()='Dashboard']")).to_be_visible()
    page.wait_for_timeout(3000)
    print("Ready to click PIM")
    page.locator("//span[normalize-space()='PIM']").click()
    print("Clicked PIM")
    page.wait_for_timeout(2000)
    expect( page.locator("//div[@class='oxd-table-filter-area']/form/div/div/div/div//label[normalize-space()='Job Title']")).to_be_visible()
    label_texts = page.locator("//div[@class='oxd-table-filter-area']/form/div/div/div/div//label").all()

    for label in label_texts:
        print(label.inner_text())
        if label.inner_text() == 'Job Title':
            page.locator(" //div[contains(@class,'oxd-grid-item')][.//label[normalize-space()='Job Title']]//i").click()
            print("Clicked drp down icon Job Title")
            break

    page.wait_for_timeout(3000)
    print("\n --->Printing the bootstrap-hidden checkbox options--->")

    bootstrap_options = page.locator("//div[@role='listbox']/div/span")

    count = bootstrap_options.count() # get the cout of options
    print("The count is:", count)  # get the cout of options
    page.wait_for_timeout(2000)

    # we need to use locator only for assertions in playwright, below is one of the type assertion
    expect(bootstrap_options).to_have_count(count)

    inside_options = bootstrap_options.all_inner_texts() # return list of inner texts
    print("Inside options:", inside_options)

    # iterating one by one option by using for loop
    for option in inside_options:
        print(option)

    # now select Automation Tester option in the drop down
    print("\n --->By using all() method the bootstrap-hidden checkbox options--->")
    print(bootstrap_options.all())
    print("printed by using all() method ")

    page.wait_for_timeout(2000)

    bootstrap_options = page.locator("//div[@role='listbox']/div/span")

    count = bootstrap_options.count()  # get the cout of options
    print("The count is:", count)  # get the cout of options
    page.wait_for_timeout(2000)

    bootstrap_options = page.locator("//div[@role='listbox']/div")

    count = bootstrap_options.count()
    print("The count is:", count)

    for i in range(count):
        text = bootstrap_options.nth(i).inner_text()
        # used this for debugging, to capture HTML elements
        print(bootstrap_options.nth(i).evaluate("(el) => el.outerHTML"))
        print(i, "---->", text)

        if text.strip() == "QA Engineer":
            print("Found QA Engineer")
            bootstrap_options.nth(i).click(force=True)
            print("Clicked QA Engineer")
            break

    page.wait_for_timeout(2000)


    # for option in bootstrap_options.all_inner_texts():
    #     if option == 'Automation Tester':
    #         bootstrap_options.filter(has_text='Automation Tester').click()
    #         print("clicked Automation Tester option")
    #         page.wait_for_timeout(2000)
    #         break
    # page.wait_for_timeout(3000)


















