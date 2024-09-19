import re
import selectorVariables as sv
from playwright.sync_api import Playwright, sync_playwright, expect

# decorator -> login
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    pl = page.locator
    page.goto(sv.url)
    pl(sv.username).click()
    pl(sv.username).fill(sv.usernameDefault)
    pl(sv.password).click()
    pl(sv.password).fill(sv.passwordDefault)
    pl(sv.loginButton).click()
    pl(sv.addToCartButton).click()
    pl(sv.shoppingCartLink).click()
    pl(sv.checkout).click()
    pl(sv.firstName).click()
    pl(sv.firstName).fill(sv.firstNameValue)
    pl(sv.firstName).press(sv.tabButton)
    pl(sv.lastName).fill(sv.lastNameValue)
    pl(sv.lastName).press(sv.tabButton)
    pl(sv.postalCode).fill(sv.postalCodeValue)
    pl(sv.continueButton).click()
    pl(sv.finish).click()
    pl(sv.backToProducts).click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="sauceTrace2.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
