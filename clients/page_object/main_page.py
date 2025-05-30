from clients.page_object.base_page import BasePage


class MainPage(BasePage):
    def open_homepage(self):
        self.page.goto("https://www.automationexercise.com/")

    def click_products_button(self):
        self.page.is_visible("a[href='/products']")
        self.page.click("a[href='/products']")
