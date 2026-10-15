import pytest
from playwright.sync_api import sync_playwright, expect, Page


'''
Automated by using this application 
file:///C:/Users/shara/Downloads/Day24-Assignment.pdf
'''

def test_flipkart_search(page: Page):

    # 1. Open Flipkart
    page.goto("https://www.flipkart.com/")
    page.wait_for_timeout(1000)

    # 2. Locate search box and type Smart
    search_box = page.locator(
        "//form[@action='/search']/div//input[contains(@title,'Search for Products')]"
    )

    search_box.fill("Smart")
    print("Filled Smart in search")

    page.wait_for_timeout(1000)

    # 3. Get all auto-suggestion options
    suggest_options = page.locator(
        "//div[contains(@class,'VDtK0l')]"
    )

    # 4. Get number of suggestions
    count = suggest_options.count()

    print("The total count of suggested options is:", count)

    page.wait_for_timeout(3000)
    assert count > 0, "count is less than 0"

    print("----> Capturing 5th option is:--->")
    for i in range(count):
        if i == 4:
            fifth_option = suggest_options.nth(i).inner_text()
            print("5th option is:", fifth_option)
            break
    page.wait_for_timeout(2000)


    # if count >= 5:
    #     fifth_option = suggest_options.nth(4).inner_text()
    #     print("---->The 5th option is:--->", fifth_option)


    # 5. Print all suggestions
    for i in range(count):

        text = suggest_options.nth(i).inner_text().strip()

        print(i, "--->", text)

    page.wait_for_timeout(2000)

    # 6. Click smartphone suggestion
    print("\n Ready to click smartphone")
    for i in range(count):

        text = suggest_options.nth(i).inner_text().strip()

        print(i, "--->", text)
        if text.lower() == "smartphone":
            print("Smartphone found")
            suggest_options.nth(i).click(force=True)
            break

    page.wait_for_timeout(2000)






