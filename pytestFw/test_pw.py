from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev")
        assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
        browser.close()

if __name__ == "__main__":
    test_example()
