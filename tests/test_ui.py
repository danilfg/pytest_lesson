from time import sleep

from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_add_products(page, base_url):
    home = HomePage(page, base_url)
    home.open()
    home.go_to_products()

    products = ProductsPage(page, base_url)
    products.wait_loaded()

    products.add_to_cart_by_id(1)
    sleep(3)
