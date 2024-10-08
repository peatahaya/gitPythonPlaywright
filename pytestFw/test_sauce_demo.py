from playwright.sync_api import Page, expect


def test_login_with_valid_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()


    # page.get_by_role("button", name="Open Menu").click()
    # page.locator("[data-test=\"logout-sidebar-link\"]").click()

    print("Test completed")