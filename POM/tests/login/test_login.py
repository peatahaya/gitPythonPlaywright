import re
from playwright.sync_api import Page, expect
from POM.src.pages.LoginPage import LoginPage
from POM.tests.data import username, password, usernameInvalid

# function that tests login with valid user data
def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text("Products")
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

# fuction that tests login with invalid user data
def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': usernameInvalid, 'password': password}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    expected_fail_message = "Username and password do not match any user in this service"
    expect(login_p.err_msg_loc).to_contain_text(expected_fail_message)
    expect(page).to_have_url('https://www.saucedemo.com/')

# function that tests login with empty login fields
def test_login_with_no_credentials(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_p = LoginPage(page)
    login_p.click_login()
    expected_fail_message = "Username is required"
    expect(login_p.err_msg_loc).to_contain_text(expected_fail_message)
    expect(page).to_have_url('https://www.saucedemo.com/')

# Test comment