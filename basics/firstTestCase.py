import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Main function
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Zaakceptuj wszystko").click()
    page.get_by_label("Szukaj", exact=True).click()
    page.get_by_label("Szukaj", exact=True).fill("playwright")
    page.goto("https://www.google.com/search?q=playwright&sca_esv=7348c2b43ef6e7ff&source=hp&ei=6TblZrezBpKsxc8P77KV-AQ&iflsig=AL9hbdgAAAAAZuVE-eRTG6Drf3XKtMYQpjZJo0EiImZv&ved=0ahUKEwj3y_nI8MGIAxUSVvEDHW9ZBU8Q4dUDCA8&uact=5&oq=playwright&gs_lp=Egdnd3Mtd2l6IgpwbGF5d3JpZ2h0MgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEieuwFQnBFYgSBwAngAkAEBmAHBAqABmhCqAQcwLjYuMi4yuAEDyAEA-AEBmAILoAKYDqgCCsICChAAGAMY6gIYjwHCAgoQLhgDGOoCGI8BwgIOEAAYgAQYsQMYgwEYigXCAggQABiABBixA8ICERAuGIAEGLEDGNEDGIMBGMcBwgIOEC4YgAQYsQMYgwEYigXCAgsQLhiABBixAxiDAcICBxAAGIAEGArCAgsQLhiABBjRAxjHAZgDDJIHBzIuNi4yLjGgB_1D&sclient=gws-wiz")
    page.get_by_role("link", name="Playwright: Fast and reliable").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
