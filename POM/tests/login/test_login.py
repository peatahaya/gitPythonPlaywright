import re
from playwright.sync_api import Page, expect


def test_login_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    products_header = page.locator("span.title")

    expect(products_header).to_have_text("Products")

def test_login_with_invalid_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    expected_fail_message = "Username and password do not match any user in this service"
    err_msg_loc = page.locator("//h3[@data-test='error']")

    expect(err_msg_loc).to_contain_text(expected_fail_message)

def test_login_with_no_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Login").click()

    expected_fail_message = "Username is required"
    err_msg_loc = page.locator("//h3[@data-test='error']")

    expect(err_msg_loc).to_contain_text(expected_fail_message)
