import pytest
from playwright.sync_api import sync_playwright, expect,Page


def test_dynamic_button(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    start_button_text = page.locator("//button[contains(@name, 'st')]")
    print("the text is:", start_button_text.inner_text())
    start_button_text.click()

    stop_button_text = page.locator("//button[contains(@name, 'st')]")
    print("the text is:", stop_button_text.inner_text())



