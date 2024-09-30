from POM.src.pages.CheckoutPage import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self._item_name = page.locator("[data-test=\"inventory-item-name\"]")
        self._item_desc = page.locator("[data-test=\"inventory-item-desc\"]")
        self._item_price = page.locator("[data-test=\"inventory-item-price\"]")
        self._remove_btn = page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")
        self._inventory_item = page.locator("[data-test=\"inventory-item\"]")
        self._checkout_btn = page.locator("[data-test=\"checkout\"]")

    def click_remove_btn(self):
        self._remove_btn.click()

    def click_checkout(self):
        self._checkout_btn.click()
        return CheckoutPage(self.page)
