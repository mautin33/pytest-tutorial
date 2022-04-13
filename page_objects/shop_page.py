from seleniumbase import BaseCase

class ShopPage(BaseCase):
    search_input = "#woocommerce-product-search-field-0"
    search_btn = "button[value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_products_Txt = ".woocommerce-info"

    #urls
    shopUrl = "https://practice.automationbro.com/shop"

    def open_page(self):
        self.open(self.shopUrl)

    