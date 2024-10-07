from POM.tests.data import first_name, last_name, postal_code


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("[data-test=\"firstName\"]")
        self._last_name = page.locator("[data-test=\"lastName\"]")
        self._postal_code = page.locator("[data-test=\"postalCode\"]")
        self._continue_btn = page.locator("[data-test=\"continue\"]")
        # self._price_value = page.locator("[data-test=\"subtotal-label\"]").inner_text()
        self._finish_btn = page.locator("[data-test=\"finish\"]")
        self._back_to_products_btn = page.locator("[data-test=\"back-to-products\"]")


    def enter_first_name(self):
        self._first_name.click()
        self._first_name.fill(first_name)

    def enter_last_name(self):
        self._last_name.click()
        self._last_name.fill(last_name)

    def enter_postal_code(self):
        self._postal_code.click()
        self._postal_code.fill(postal_code)

    def click_continue(self):
        self._continue_btn.click()

    def confirm_data(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_postal_code()
        self.click_continue()

    def click_finish(self):
        self._finish_btn.click()

    def click_back_to_products(self):
        self._back_to_products_btn.click()

