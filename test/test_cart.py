from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys

class CartTest(CartPage):
    # Setup 
    def setUp(self):
        super().setUp()
        print("Running before each test")

        self.openShop()


    # # TearDown
    # def tearDown(self):
    #     print("Running after each test")

    #     super().tearDown()


    def test_add_to_cart(self):

        # add item to the cart.
        self.click(self.converse_add_to_cart_btn)

        # assert product is added to the cart.
        self.assert_text('1',self.cart_count_txt)

        # open cart page.
        self.openPage()

        # get current subtotal.
        text = self.get_text(self.subtotal_text)
        print(text)

        # change cart quantity.
        self.set_value(self.product_quantity_input, '2')
        self.send_keys(self.product_quantity_input, Keys.RETURN)
        self.click(self.update_cart_btn)

        #wait few seconds
        #bad practice
        # time.sleep(5)


        # wait for loading to be completed
        # self.wait_for_element_visible(self.loading_overlay)
        # self.wait_for_element_not_visible(self.loading_overlay)


        # assert subtotal to be different than the original subtotal.
        self.wait_for_text("$300.00", self.subtotal_text)
        updated_text = self.get_text(self.subtotal_text)
        print(updated_text)
        self.assertNotEqual(text,updated_text)

        