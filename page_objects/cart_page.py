from seleniumbase import BaseCase

class CartPage(BaseCase):
    
    converse_add_to_cart_btn = "a[aria-label='Add “Branded Converse” to your cart']"
    cart_count_txt = "ul[id='primary-menu'] span[class='count']"
    subtotal_text = "td[class='product-subtotal']"
    product_quantity_input = "input[id^='quantity']"
    update_cart_btn = "button[name='update_cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

    #urls
    shopUrl = "https://practice.automationbro.com/shop"
    cartUrl = "https://practice.automationbro.com/cart"

    def openShop(self):
        self.open(self.shopUrl)

    def openPage(self):
        self.open(self.cartUrl) 
