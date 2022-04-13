
from page_objects.home_page import HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        # login
        self.login()
       
        # open Home page
        self.open_page()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")

        # logout
        self.logout()
        
        super().tearDown()


    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(HomePage.logo_icon)

        # click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url,"https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.",HomePage.heading_txt)

        # Scroll to button and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",HomePage.copyright_txt) 


    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        # find menu links elements
        menu_links_el = self.find_elements(HomePage.menu_links)

        #run test 
        # pytest -k "test_menu_links"    -- run a particular test.
        # pytest -k "test_menu_links" -s --print on screen.

        # loop through our menu links.
        for idx, link_el in enumerate(menu_links_el):
            print(idx, link_el.text)
            # self.assertEqual(expected_links[idx], link_el.text)










