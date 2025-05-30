from time import sleep

from clients.page_object.main_page import MainPage
from clients.page_object.products_page import ProductsPage


def test_search_products(page):
    main_page = MainPage(page)
    main_page.open_homepage()
    main_page.verify_homepage_visible()

    main_page.click_products_button()
    main_page.verify_homepage_visible()

    product_page = ProductsPage(page)
    product_page.enter_search("Blue Top")
    product_page.click_search_button()
    product_page.verify_homepage_visible()
    sleep(3)
