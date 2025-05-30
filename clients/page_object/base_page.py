from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_homepage_visible(self):
        self.page.wait_for_load_state("load", timeout=5000)
