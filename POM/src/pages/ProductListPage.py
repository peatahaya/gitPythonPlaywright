from POM.src.pages.CartPage import CartPage

class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator('#logout_sidebar_link')
        self._item = page.locator("[data-test=\"item-0-title-link\"]")
        self._add_to_cart_btn = page.locator("[data-test=\"add-to-cart\"]")
        self._cart_btn = page.locator("[data-test=\"shopping-cart-link\"]")

    @property
    def product_header(self):
        """It returns locator or selector for product
        header text"""
        return self._products_header

    def click_burger_menu_btn(self):
        """Clicks on burger menu icon from header"""
        self._burger_menu.click()

    def click_logout(self):
        """Clicks on logout"""
        self._logout_btn.click()

    def do_logout(self):
        """Logout from the sauce demo"""
        self.click_burger_menu_btn()
        self.click_logout()

    def click_item(self):
        self._item.click()

    def click_add_to_cart_btn(self):
        self._add_to_cart_btn.click()

    def click_cart_btn(self):
        self._cart_btn.click()
        return CartPage(self.page)