import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_single_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)
    page.locator("select#country").select_option(value="canada")
    page.wait_for_timeout(1000)
    page.locator("select#country").select_option(index=4)
    page.wait_for_timeout(1000)
    page.locator("select#country").select_option(label="India")
    page.wait_for_timeout(1000)
    # To get to know which one is selected by using input_value() like get_attribute() in selenium
    Selected_label = page.locator("select#country").input_value()
    print("The selected is:",Selected_label)

    '''
       # verify how many options are listed in dropdown by using xpath
       # this is the syntax of css for the same : select#colors option
       # we have two methods both will return list 
       # for single element  inner_text() vs text_content() 
       # inner text gives clean one without spaces whereas text_content() will return with spaces in list
       # inorder to capture multiple elements 
       # we have all_inner_text() vs all_text_content() 
       # and we have one more method is all()  
    '''
