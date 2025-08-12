from pages.base_page import BasePage


class HomePage(BasePage):
    PRODUCT_LINK = "a[href='/products']"

    def open(self):
        self.goto()
        self.page.wait_for_load_state("domcontentloaded")

    def go_to_products(self):
        self.page.click(self.PRODUCT_LINK)
