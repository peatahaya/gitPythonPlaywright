import re
from playwright.sync_api import Page, expect
from POM.tests.data import username, password, usernameInvalid
from POM.src.pages.LoginPage import LoginPage
from POM.src.pages.ProductListPage import ProductListPage

def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.do_logout()
    expect(login_p.login_button).to_be_visible()