import re
from playwright.sync_api import Page, expect
from POM.src.pages.LoginPage import LoginPage
from POM.tests.data import username, password, usernameInvalid, inventory_url, item_url, cart_url, item_name, item_desc, \
    item_price, checkout_step_one_url, checkout_step_two_url, checkout_complete_url, main_url
from POM.src.pages.CartPage import CartPage


def test_end_to_end_flow(set_up_tear_down) -> None:
    page = set_up_tear_down
    expect(page).to_have_url(main_url)
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    expect(page).to_have_url(inventory_url)
    products_p.click_item()

    expect(page).to_have_url(item_url)
    products_p.click_add_to_cart_btn()
    cart_p = products_p.click_cart_btn()

    expect(page).to_have_url(cart_url)
    expect(cart_p._item_name).to_contain_text(item_name)
    expect(cart_p._item_desc).to_contain_text(item_desc)
    expect(cart_p._item_price).to_contain_text(item_price)
    checkout_p = cart_p.click_checkout()

    expect(page).to_have_url(checkout_step_one_url)
    checkout_p.confirm_data()

    expect(page).to_have_url(checkout_step_two_url)
    # checkout_p.print_value()
    # expect(checkout_p._price_value).to_contain_text('9.99')
    checkout_p.click_finish()

    expect(page).to_have_url(checkout_complete_url)
    checkout_p.click_back_to_products()
    expect(page).to_have_url(inventory_url)

