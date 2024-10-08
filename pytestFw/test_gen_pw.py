import re
from playwright.sync_api import Page, expect


def test_element_visibility(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.get_by_text("This is just a demo of")).to_be_visible()

def test_element_contians_text(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.get_by_role("heading")).to_contain_text("todos")

def test_proper_list_element_display(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("water the plants")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("water the plants")
