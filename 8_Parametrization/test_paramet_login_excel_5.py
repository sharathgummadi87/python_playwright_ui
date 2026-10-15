import pytest
from playwright.sync_api import expect,Page
import json
import csv
import openpyxl


'''
When working with excel files is very important 
the order is ::  workbook(excel file)  --> sheet(ex:in excel file like sheet1, sheet2) -> cell(data)
we need to have openpyxl module to be installed through
 pip install openpyxl -> to install
 pip list -> check 
'''

test_data = []

filepath = 'C:\\Users\\shara\\PycharmProjects\\Python_Playwright\\8_Parametrization\\login_test_data2.xlsx'
workbook = openpyxl.load_workbook(filepath)
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    test_data.append(row)

@pytest.mark.parametrize("email, password, validity", test_data)
def test_login_test(email, password, validity, page:Page):


    page.goto("https://demowebshop.tricentis.com/login")

    login_link = page.locator("//a[normalize-space()='Log in']")
    expect(login_link).to_be_visible()
    page.wait_for_load_state()

    input_text = page.locator("//input[@id='Email']")
    input_text.fill(email)

    password_input = page.locator("//input[@id='Password']")
    password_input.fill(password)

    login_button = page.locator("//input[@value='Log in']")
    login_button.click()
    page.wait_for_load_state()

    if validity.lower() == 'valid':
        logout_button = page.locator("//a[normalize-space()='Log out']")
        expect(logout_button).to_be_visible()
        print("Logout button is visible")
    else:
        error_text = page.locator("//span[normalize-space() = 'Login was unsuccessful. Please correct the errors and try again.']")
        expect(error_text).to_be_visible()
        print("No account is found in our database, please register")
