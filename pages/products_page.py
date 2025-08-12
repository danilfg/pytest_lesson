from playwright.sync_api import expect

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def wait_loaded(self):
        expect(self.page.locator("h2.title:has-text('All Products')")).to_be_visible()

    def add_to_cart_by_id(self, product_id: int):
        btn = self.page.locator(
            f".productinfo >> a.btn.add-to-cart[data-product-id='{product_id}']"
        )
        btn.is_visible()
        btn.click()
        modal = self.page.locator("#cartModal")
        expect(modal).to_be_visible()
        self.page.click("a:has-text('View Cart')")
