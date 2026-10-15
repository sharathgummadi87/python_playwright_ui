import pytest
from playwright.sync_api import Page, expect


def select_date(page, target_year, target_month, target_date, is_date_future):

    print(":::: Test has started :::::")
    while True:

        current_month = page.locator("//span[@class='ui-datepicker-month']").text_content()
        current_year = page.locator("//span[@class='ui-datepicker-year']").text_content()

        if current_month == target_month and current_year == target_year:
            break
        if is_date_future == True:
            page.locator("//span[normalize-space()='Next']/parent::a").click()
        else:
            page.locator("//span[normalize-space()='Prev']/parent::a").click()

    all_dates = page.locator("//table[@class='ui-datepicker-calendar']/tbody/tr/td/a").all()
    # return list of locators

    for day in all_dates:
        datee = day.inner_text()
        if datee == target_date:
            print("The datee variable expected is locator inner text:", datee)
            day.click()
            print("Date is selected")
            break








def test_jquery_datepicker(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    # page.locator("//input[@id='datepicker']").fill("10/5/2026")
    #
    # input = page.locator("//input[@id='datepicker']").input_value()
    # print("\nThe date is given--->",input)

    page.wait_for_timeout(2000)

    page.locator("//input[@id='datepicker']").click() #opens date picker
    print("\nThe date picker is clicked--->")
    page.wait_for_timeout(3000)

    year = '2020'
    month = 'November'
    date = '24'
    is_date_future = False
    print("Calling function")
    page.wait_for_timeout(2000)
    select_date(page, year, month, date, is_date_future)

    input_selected = page.locator("//input[@id='datepicker']").input_value()
    print("\nThe date is selected is::",input_selected)