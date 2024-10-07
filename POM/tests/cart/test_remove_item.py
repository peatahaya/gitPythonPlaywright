from playwright.sync_api import Page, expect
from POM.src.pages.LoginPage import LoginPage
from POM.tests.data import username, password, usernameInvalid, inventory_url, main_url, item_url, cart_url, item_name, item_desc, \
    item_price


# function that tests removing previosly added item from cart
def test_add_and_remove_item(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    expect(page).to_have_url(main_url)
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
    cart_p.click_remove_btn()
    expect(cart_p._inventory_item).not_to_be_visible()