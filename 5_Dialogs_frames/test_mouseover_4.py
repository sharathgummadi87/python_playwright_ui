from playwright.sync_api import sync_playwright, expect,Page
import pytest


@pytest.mark.skip
def test_dynamic_button(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointme = page.locator("//button[@class='dropbtn']")
    pointme.hover()

    # laptops = page.locator("//div[@class='dropdown']//a[normalize-space()='Laptops']")
    laptops = page.locator("//a[normalize-space()='Laptops']/parent::div[@class='dropdown-content']")
    laptops.hover()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto("http://swisnl.github.io/jQuery-contextMenu/demo.html")

    button=page.locator("//span[normalize-space()='right click me']")
    button.click(button='right')  # performs right click action - right , left, middle

    page.wait_for_timeout(5000)


def test_mouse_doubleclick(page:Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    copy_txt = page.locator("//button[@ondblclick='myFunction1()']")
    copy_txt.dblclick()

    print("done")
    get_text = page.locator("//input[@id='field2']")
    text = get_text.input_value()  # Gets the input value present in the input field
    print(text)
    page.wait_for_timeout(3000)


def test_mouse_draganddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source=page.locator("//div[@id='draggable']")
    target=page.locator("//div[@id='droppable']")
    source.drag_to(target)

    page.wait_for_timeout(5000)

