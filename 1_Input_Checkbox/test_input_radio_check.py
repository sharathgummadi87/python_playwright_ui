from playwright.sync_api import Page, expect
import pytest


def test_input_radio_check(page: Page):

    page.goto("https://practice-automation.com/form-fields/")
    page.wait_for_timeout(1000)
    # Name input field
    page.get_by_test_id("name-input").fill("kumar")
    # expect(page.locator("input#name-input")).to_be_visible()
    # page.locator("input#name-input").fill("kumar")
    # page.locator("//input[@id='name-input']").fill("kumar")

    # password input field
    page.get_by_label("Password").fill("Test12")
    page.wait_for_timeout(1000)

    # check_a =  page.get_by_role("checkbox", name='Water').check()
    # check_a.check()
    # expect(check_a).to_be_checked()
    # expect(check_a).not_to_be_checked()

    print("Check box verification")
    data = ["Water", "Milk", "Coffee"]

    for i in data:
        page.locator(f"//input[@type='checkbox' and @value='{i}']").check()


    page.wait_for_timeout(1000)
    expect(page.get_by_text("What is your favorite color?")).to_be_visible()
    page.wait_for_timeout(1000)
    page.get_by_text("What is your favorite color?").text_content()
    page.wait_for_timeout(1000)

    print("radio button verification")


    text = page.get_by_text("What is your favorite color?").text_content()
    print(text)

    data2 = ["Red", "Blue", "Yellow", "Green"]
    radio_button = page.locator("//input[@type='radio']")
    print("Total radio button count is:",radio_button.count())
    radio_buttons = radio_button.all()
    print(radio_buttons)
    print()
    for i in data2:
        page.locator(f"//input[@type='radio' and @value='{i}']").click()
        page.wait_for_timeout(2000)
    print("DropDown verification")
    page.locator("select[id='automation']").select_option("No")
    page.wait_for_timeout(3000)
    print("No selected")
    page.locator("select[id='automation']").select_option("Yes")
    print("Yes selected")
    page.wait_for_timeout(3000)
    print("trying to capture options in dropdown filed")
    '''
    # This is written common xpath for all the options in select class dropdown and used all_text_contents() method 
    # to get the DOM Or HTML locator elements in the list format so that I can refer in validations..... 
    Generally we do write assert operations for locators and can not do assert for values in playwright
    
    '''
    dropdown_options = page.locator("//select[@id='automation']/option").all_text_contents()
    # The below loop prints options one by one
    count = 0
    for option in dropdown_options:
        print(option)
        count = count+1
    print("The total number of options is:", count)

    # To count how many options are displayed in select drop down
    # count = 0
    # for i in range(dropdown_options.count()):
    #     count = count+1
    page.get_by_test_id("email").fill("Test12@gmail.com")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Enter message here").fill("ItsGK")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name='submit').click()
    page.wait_for_timeout(2000)
    print("Submit button clicked")









