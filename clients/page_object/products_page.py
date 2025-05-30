from clients.page_object.base_page import BasePage


class ProductsPage(BasePage):
    def enter_search(self, product_name):
        self.page.fill("input[id='search_product']", product_name)

    def click_search_button(self):
        self.page.click("button[id='submit_search']")
