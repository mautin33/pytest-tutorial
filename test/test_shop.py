from page_objects.shop_page import ShopPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException #import exception


class ShopTest(ShopPage):
    def test_search_products(self):
        #open page
        self.open_page()

        #search for product
        self.send_keys(self.search_input,"Toys")
        self.click(self.search_btn)


        #assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException:
            self.assert_text("No product were found matching your selection",self.no_products_Txt)

            