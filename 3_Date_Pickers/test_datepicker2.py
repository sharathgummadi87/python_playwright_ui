import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError



def select_checkin_date(page, target_year, target_month, target_day):

    while True:

        print(":::::select_checkin_date Function got started ::::")
        check_in = page.locator("//span[@data-testid='date-display-field-start']")
        print("Check-in text:", check_in.inner_text())

        page.wait_for_timeout(3000)

        # Checking and Selecting the month
        print("Ready to checkin the month:")
        checkin_month = page.locator(
            f"//div[@data-testid='searchbox-datepicker-calendar']"
            f"//h3[contains(@id,'bui-calendar-month') and normalize-space()='{target_month}']")
        page.wait_for_timeout(1000)
        count = checkin_month.count()
        if count > 0:
            print("The checkin month found")
            print("The checkin_month text is:",checkin_month.inner_text())
            break

        next_button = page.locator("//button[@aria-label='Next month']")
        next_button.click()
        print("next button is clicked")


    #came out from the while loop and if Im in the loop it will consider below code in the while loop
    # so if any of the below locator is not found then test would get failed
    # Checking and Selecting the date
    checkin_date = page.locator(f"//div[@id='calendar-searchboxdatepicker']"
                     f"//div//h3[normalize-space() = '{target_month}']/following-sibling::table[contains(@aria-labelledby,'bui-calendar-month')]"
                     f"//tbody/tr//td[contains(@aria-label, '{target_day}')]")

    print("date text is:", checkin_date.inner_text())
    page.wait_for_timeout(1000)
    checkin_date.click()
    # re-verifying selected date is expected
    selected_date = page.locator("//span[@data-testid='date-display-field-start']")
    date_text = selected_date.inner_text()
    print("The selected date is:", date_text)
    expect(page.locator("//span[@data-testid='date-display-field-start']")).to_contain_text(date_text)
    page.wait_for_timeout(3000)



def select_checkout_date(page, year_c, month_c, day_c):

    while True:

        # opening calender-checkout field
        print("::::Checkout execution is started::::")

        check_out = page.locator("//span[@data-testid='date-display-field-end']")
        print("Checkout text:", check_out.inner_text())

        # Checking and Selecting the month
        month_check = page.locator(f"//div[@data-testid='searchbox-datepicker-calendar']"
                                   f"//h3[contains(@id,'bui-calendar-month') and normalize-space()='{month_c}']")

        count = month_check.count()
        print("count is :", count)

        if count > 0:
            print("Month is found")
            print("Month inner text is:", month_check.inner_text())
            break

        next_button = page.locator("//button[@aria-label='Next month']")

        print("next_button count:", next_button.count())

        next_button.click()
        print("next button is clicked")

    # Checking and Selecting the date
    Checkout_date = page.locator(f"//div[@id='calendar-searchboxdatepicker']"
                         f"//div//h3[normalize-space() = '{month_c}']/following-sibling::table[contains(@aria-labelledby,'bui-calendar-month')]"
                         f"//tbody/tr//td[contains(@aria-label, '{day_c}')]")

    print("Checkout_date count is:", Checkout_date.count())
    print("Checkout_date text is:", Checkout_date.inner_text())
    page.wait_for_timeout(2000)

    Checkout_date.click()
    selected_date = page.locator("//span[@data-testid='date-display-field-end']")
    Checkout_date = selected_date.inner_text()
    print("The selected date is:", Checkout_date)
    page.wait_for_timeout(3000)



def test_date_picker2(page):

    page.goto("https://www.booking.com/")
    # page.goto("https://www.booking.com")

    close_prompt = page.locator("//button[contains(@aria-label, 'Dismiss sign-in info.')]")

    try:
        close_prompt.wait_for(state="visible", timeout=5000)
        close_prompt.click()
        close_prompt.wait_for(state="hidden", timeout=5000)
        print("close_prompt is appeared and closed properly")

    except PlaywrightTimeoutError:
        print("Did not appeared close_prompt")

    print("Current URL:", page.url)
    print("Page title:", page.title())

    page.screenshot(path="debug.png", full_page=True)

    select_dates = page.locator("//span[normalize-space()='Select dates']")
    select_dates.wait_for(state='visible', timeout=10000)
    print("Count:", select_dates.count())
    select_dates.click()
    print("Date is clicked")
    print("Inner text is:",select_dates.inner_text())
    page.wait_for_timeout(5000)

    year = '2026'
    month = 'November 2026'
    day = '13'

    print("ready to call function select_checkin_date(page, year, month, day):")
    select_checkin_date(page, year, month, day)

    year_c = '2027'
    month_c = 'January 2027'
    day_c = '15'

    select_checkout_date(page, year_c, month_c, day_c)
