import re
from playwright.sync_api import Page, expect


def xtest_logout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    products_header = page.locator("span.title")
    burger_menu = page.locator("button#react-burger-menu-btn")

    burger_menu.click()
    logout_btn = page.locator("//div[@class='bm-menu']//a[text()='Logout']")

    logout_btn.click()
    expect(page.get_by_text("Login")).to_be_visible()