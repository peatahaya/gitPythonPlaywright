import re
from playwright.sync_api import Page, expect
from POM.src.pages.LoginPage import LoginPage
from POM.tests.data import username, password, usernameInvalid
from POM.src.pages.CartPage import CartPage


def xtest_add_and_remove_item(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    products_p.click_item()
    expect(page).to_have_url('https://www.saucedemo.com/inventory-item.html?id=0')
    products_p.click_add_to_cart_btn()
    cart_p = products_p.click_cart_btn()
    expect(page).to_have_url('https://www.saucedemo.com/cart.html')
    expect(cart_p._item_name).to_contain_text("Sauce Labs Bike Light")
    expect(cart_p._item_desc).to_contain_text(
        "A red light isn't the desired state in testing but it sure helps "
        "when riding your bike at night. Water-resistant with 3 lighting modes, "
        "1 AAA battery included.")
    expect(cart_p._item_price).to_contain_text("9.99")
    cart_p.click_remove_btn()
    expect(cart_p._inventory_item).not_to_be_visible()

    # expect(products_p.product_header).to_be_visible()
    # expect(products_p.product_header).to_have_text("Products")
    # expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

def test_end_to_end_flow(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    products_p.click_item()
    expect(page).to_have_url('https://www.saucedemo.com/inventory-item.html?id=0')
    products_p.click_add_to_cart_btn()
    cart_p = products_p.click_cart_btn()
    expect(page).to_have_url('https://www.saucedemo.com/cart.html')
    expect(cart_p._item_name).to_contain_text("Sauce Labs Bike Light")
    expect(cart_p._item_desc).to_contain_text(
        "A red light isn't the desired state in testing but it sure helps "
        "when riding your bike at night. Water-resistant with 3 lighting modes, "
        "1 AAA battery included.")
    expect(cart_p._item_price).to_contain_text("9.99")
    checkout_p = cart_p.click_checkout()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')

    checkout_p.confirm_data()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')
    # checkout_p.print_value()

    # expect(checkout_p._price_value).to_contain_text('9.99')
    checkout_p.click_finish()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-complete.html')
    checkout_p.click_back_to_products()
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

