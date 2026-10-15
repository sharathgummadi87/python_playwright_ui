import pytest

from playwright.sync_api import expect,Playwright, Page

# Test data
search_items = ['laptop', 'Gift card', 'smartphone']
 #'monitor'

@pytest.mark.parametrize('item', search_items)
def test_parametrize_normal_file(item, page:Page):

    page.goto("https://demowebshop.tricentis.com/")

    # input_search box
    search_box = page.locator("//input[@id='small-searchterms']")
    search_box.fill(item)

    # Search button
    search_button = page.locator("//input[@value='Search']")
    search_button.click()

    product = page.locator(f"//h2[@class='product-title']/a[contains(translate(normalize-space(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'{item.lower()}')]")

    count = product.count()
    print("The count is:", count)

    if count > 0:
        print("Product found")

        product_text = product.first.inner_text()
        print("Product text is:", product_text)
        assert item.lower() in product_text.lower()


    page.wait_for_timeout(3000)















