import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    # register event
    def handle_dialog(dialog):
        dialog.accept()

    # page.on() will perform handles the events or dialogs
    page.on("dialog",handle_dialog)
    page.wait_for_timeout(5000)
    # it clicks the simple alert on the above url webpage
    # but before clicking we have to register an event
    # because unless we register an event the promot does not display in UI
    # register event is can be created by using 2 ways by creating method or lambda function
    page.locator("//button[@id='alertBtn']").click()
    page.wait_for_timeout(5000)


@pytest.mark.skip
def test_simple_dialog_using_lambda(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # register event
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog",handle_dialog)


    #syntax: lambda parameter : expression
    page.on("dialog", lambda dialog: dialog.accept())

    page.wait_for_timeout(5000)

    page.locator("//button[@id='alertBtn']").click() # clicking on the button which will open dialog
    page.wait_for_timeout(5000)


def test_confirm_button(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(5000)

    page.locator("//button[@id='confirmBtn']").click()
    page.wait_for_timeout(4000)
    cancel_text = page.locator("//p[@id='demo']")
    print(cancel_text.inner_text())
    expect(cancel_text).to_contain_text("You pressed Cancel!")


def test_prompt_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialog: dialog.accept('kumar'))
    page.locator("#promptBtn").click()  # clicking on the button which will open dialog
    page.wait_for_timeout(3000)

    text=page.locator("#demo").inner_text()
    print("Output text:", text)

    expect(page.locator("#demo")).to_have_text("Hello kumar! How are you today?")

    page.wait_for_timeout(5000)


