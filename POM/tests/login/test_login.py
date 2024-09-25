import re
from playwright.sync_api import Page, expect

from POM.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text("Products")

def xtest_login_with_invalid_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    expected_fail_message = "Username and password do not match any user in this service"
    err_msg_loc = page.locator("//h3[@data-test='error']")

    expect(err_msg_loc).to_contain_text(expected_fail_message)

def xtest_login_with_no_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Login").click()

    expected_fail_message = "Username is required"
    err_msg_loc = page.locator("//h3[@data-test='error']")

    expect(err_msg_loc).to_contain_text(expected_fail_message)
