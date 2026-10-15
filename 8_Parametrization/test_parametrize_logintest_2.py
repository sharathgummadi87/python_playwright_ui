import pytest
from playwright.sync_api import expect,Page


# Test data
login_test_data = [
    ("laura.taylor1234@example.com", "test123", "valid"),
    ("invaliduser@example.com", "test321", "invalid"),
    ("validuser@example.com", "testxyz", "invalid"),
    ("", "", "invalid")]


@pytest.mark.parametrize("email, password, validity", login_test_data)
def test_login_test(email, password, validity,page:Page):

    page.goto("https://demowebshop.tricentis.com/login")

    login_link = page.locator("//a[normalize-space()='Log in']")
    expect(login_link).to_be_visible()
    page.wait_for_load_state()

    input_text = page.locator("//input[@id='Email']")
    input_text.fill(email)
    page.wait_for_load_state()

    password_input = page.locator("//input[@id='Password']")
    password_input.fill(password)
    page.wait_for_load_state()

    login_button = page.locator("//input[@value='Log in']")
    login_button.click()
    page.wait_for_load_state()

    if validity.lower() == 'valid':
        logout_button = page.locator("//a[normalize-space()='Log out']")
        expect(logout_button).to_be_visible(timeout=5000)
        print("Logout button is visible")
    else:
        error_text = page.locator("//span[normalize-space() = 'Login was unsuccessful. Please correct the errors and try again.']")
        expect(error_text).to_be_visible(timeout=5000)
        print("No account is found in our database, please register")










