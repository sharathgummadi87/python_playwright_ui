import pytest
from playwright.sync_api import sync_playwright, expect, Page


'''
Automated by using this application 
file:///C:/Users/shara/Downloads/Day23-Dropdown+assignments-1.pdf 
'''

def test_multi_dropdown(page: Page):
    page.goto("https://www.bstackdemo.com/")
    page.wait_for_timeout(1000)

    # Locate and Verify Dropdown
    expect(page.locator("div.sort")).to_be_visible()
    expect(page.locator("div.sort")).to_be_enabled()

    # Sort Products lowest to highest
    # Select the "Lowest to highest" option from the dropdown.
    # this is the xpath to display all dropdown options //div[@class='sort']/select/option


    print("To display options available in select drop-down")
    data_drop = page.locator("div.sort select option").all_inner_texts()
    print("The data is :",data_drop)
    for i in data_drop:
        print(i)

    page.locator("div.sort select").select_option(label='Lowest to highest')
    page.wait_for_timeout(2000)
    print("Lowest to highest is selected")
    '''
        # Extract Product Data
        # Capture all product prices and product names using locators: 
        # by using prices, product names
    '''
    print("\n<-capturing how many products are listed->\n")

    total_products = page.locator("//div[@class='shelf-item']")
    product_count = total_products.count()
    print("The total products count is :",product_count)

    print("\n->Capturing one by one Product Name & it's Price \n->")
    product_names = page.locator("//div[@class='shelf-item']/p").all_inner_texts()

    print("\n->The product names are:->\n",product_names)
    page.wait_for_timeout(2000)

    product_prices = page.locator("//div[@class='shelf-item']//div[@class='val']/b").all_inner_texts()
    print("\n ->The product prices are:->\n",product_prices)
    page.wait_for_timeout(2000)

    product_names_d = page.locator("//div[@class='shelf-item']/p").all
    d = {}
    for i in range(product_count):
        name = product_names[i]
        price = product_prices[i]
        d[name] = price
    print("The product and it's price in dict format")
    print(d)

    for k, v in d.items():
        if k == 'Pixel 2' or k == 'Galaxy S20 Ultra':
            if k == 'Pixel 2':
                print("The least product price name is :", k, "and it's price is:", v)
            else:
                print("The highest product price name is :", k, "and it's price is:", v)


























