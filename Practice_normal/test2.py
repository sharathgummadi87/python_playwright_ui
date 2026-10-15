from itertools import count

from playwright.sync_api import Page, expect


def test_launch_browser(page:Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_url("https://www.google.com/")
    expect(page).to_have_title("Google")

    page.goto("https://demowebshop.tricentis.com/desktops")
    page.wait_for_timeout(1000)
    expect(page.locator("a>img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(1000)
    text_a = page.locator("h2>a[href*='computer']").all_text_contents()
    print(text_a)
    count = 0
    n = 1
    data1 = []
    for i in text_a:
        print(f"The product {n} title is:",i)
        count = count+1
        if n == 1 or n == 4:
            data1.append(i)
        n = n+1
    print("the count is:",count)
    print("this is captured by using list extract:",data1)
    print()
    #first child using css-selector
    first_child = page.locator("div.item-box:first-child h2.product-title>a").all_text_contents()
    page.wait_for_timeout(1000)
    print("the first child is:",first_child)

    #last child using css-selector
    last_child = page.locator("div.item-box:last-child h2.product-title>a").all_text_contents()
    page.wait_for_timeout(1000)
    print("the last child is:",last_child)

    #nth child using css-selector
    # nth-child = page.locator("div.item-box:nth-child(2) h2.product-title>a").all_text_contents()
    # print("the nth child is:",nth-child)

    print("\nThe footer sections are:\n")
    # first_footer_name = page.locator("div.information").all_text_contents()
    # page.wait_for_timeout(1000)
    # print("The first footer name is:", first_footer_name)

    first_url_in = page.locator("div.column ul>li>a[href='/sitemap']").all_text_contents()
    page.wait_for_timeout(1000)
    print("The footer first Url is:",first_url_in)

    print("The footer last url")
    last_url_in = page.locator("div.column ul>li>a[href='/contactus']").all_text_contents()
    page.wait_for_timeout(1000)
    print("The footer last Url is:",last_url_in)

    # second_footer_name = page.locator("div.customer-service").all_text_contents()
    # page.wait_for_timeout(1000)
    # print("The second footer name is:",second_footer_name)


    first_url_search = page.locator("div.customer-service ul>li>a[href='/search']").all_text_contents()
    page.wait_for_timeout(1000)
    print("The second footer first link is:",first_url_search)


    last_url_search = page.locator("div.customer-service ul>li>a[href='/newproducts']").all_text_contents()
    page.wait_for_timeout(1000)
    print("The second footer first link is:",last_url_search)

    nth_seacrch = page.locator("div.customer-service ul>li:nth-child(4)>a]")
    page.wait_for_timeout(1000)
    print("The nth_search is:", nth_seacrch)






























