import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_multi_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(1000)

    # select multiple options from teh dropdown - 3 ways

    # page.locator("select#colors").select_option(label=["Red", "Blue"])
    # page.wait_for_timeout(2000)
    page.locator("select#colors").select_option(value=["red","white"])
    page.wait_for_timeout(1000)
    select_one = page.locator("select#colors").input_value()
    print(select_one)
    page.wait_for_timeout(1000)
    page.locator("select#colors").select_option(index=[5,2])
    page.wait_for_timeout(2000)

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
    all_items = page.locator("//select[@id='colors']/option").all_inner_texts()
    print("The items in dropdown field:")


    data = [i for i in all_items ]
    print(data)
    print()
    for i in all_items:
        print(i)
        if i == "Yellow":
            print("Got expected color:",i)
            break

    # data2 = page.locator("//select[@id='colors']/option").all_text_contents()
    # for i in data2:
    #     print(i)






