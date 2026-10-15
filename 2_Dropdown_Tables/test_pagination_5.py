from playwright.sync_api import expect,Page
import pytest

"""
def test_pagination_table_d(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    has_more_pages = True
    while has_more_pages:

        tables = page.locator("//table[@id='example']//tbody/tr")
        count = tables.count()
        print("-->The count is:-->",count)
        page.wait_for_timeout(2000)

        for i in range(count):
            text = tables.nth(i).inner_text()
            print(text.strip())
        page.wait_for_timeout(2000)

        #clicking the next button icon in the table
        next_button = page.locator("//div[@class='dt-paging']//button[@aria-label='Next']")

        '''
        # IMPORTANT: HTML uses aria-disabled
        # first, this "aria_disabled" attribute won't be visible until click button reaches last position
        # when next button reached last position then this attribute will appear on DOM & value will be true
        # so we can use this attribute and pass in get_attribute() method and can used in validation
        '''
        aria_disabled = next_button.get_attribute("aria-disabled")

        print("aria-disabled:", aria_disabled)

        if aria_disabled == "true":
            has_more_pages = False
            print("Last page reached. Stopping pagination.")
        else:
            next_button.click()

    page.wait_for_timeout(3000)

"""


# This is the best practice for xpath tables by using dynamic xpath
def test_pagination_table_office(page:Page):
    print("\n Test case 1::find the employee office city name where the employee name is Cara Stevens ")

    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    name = "Cara Stevens"
    '''
    # It finds entire Cara Stevens row and see difference between this two xpaths
    #//table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']-> finds only cara stevens name.
    #//table[@id='example']//tbody/tr[td[normalize-space()='Cara Stevens']]-> finds entire row where cara stevens name presents.
       or 
    # f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']/parent::tr" -> traversing approach,
                this one also finds entire row where cara stevens name presents
    '''

    # Find the Name of the employee
    cara_name = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']")
    print("The name of employee is:", cara_name.inner_text())

    # Find entire row the Name of the employee
    cara_row = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{name}']/parent::tr")

    print("\nThe employee row is:\n", cara_row.inner_text())

    page.wait_for_timeout(3000)

    '''
   
    # Finding Office column header on cara stevens row 
    # because we need to have td[coulum number]  or td[i] in below line 
    # //table[@id='example']//tbody/tr/td[normalize-space()='Cara Stevens']/td[i]
    # so far found Cara Stevens row and need to find column that has to be dyamic one only 

    '''
    # Find office city name of the employee by using locator chaining concept
    # example instead writing of cara_row locator above just use that variable locator object

    city = cara_row.locator("xpath=.//td[count(//table[@id='example']//thead/tr/th[normalize-space()='Office']/preceding-sibling::th) + 1]")

    print("The office is :", city.inner_text())

    page.wait_for_timeout(3000)


  #  //table[@id='example']//tbody/tr/td[normalize-space()='Edinburgh']/parent::tr

# This is the best practice for xpath tables by using dynamic xpath
def test_pagination_table_name(page: Page):
    print("\n Test case::find the employee name where the office name is Edinburgh ")
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    office = "Edinburgh"

    # Find the Name of the employee
    emp_office = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{office}']")
    print("The employee office name is:", emp_office.inner_text())


    # this will finds office row of the employee which we want to find the employee name
    office_row = page.locator(f"//table[@id='example']//tbody/tr/td[normalize-space()='{office}']/parent::tr")

    print("\nThe office row is:\n", office_row.inner_text())

    page.wait_for_timeout(3000)

    # Find name of employee using locator chaining concept
    # example instead writing of office_row locator above just use that variable locator object

    emp_name = office_row.locator("xpath=.//td[count(//table[@id='example']//thead/tr/th[normalize-space()='Name']/preceding-sibling::th) + 1]")
    print("The name of employee is :", emp_name.inner_text())

    page.wait_for_timeout(3000)




















