from seleniumbase import BaseCase

class HomePage(BaseCase):
    #selectors
    logo_icon = ".custom-logo-link"
    get_started_btn = "#get-started"
    heading_txt = "h1"
    copyright_txt = ".tg-site-footer-section-1"
    menu_links = "//*[starts-with(@id, 'menu-item')]"
    username = "#username"
    passwd = "#password"
    login_btn = "button[name=login]"
    logout_btn = ".woocommerce-MyAccount-content a[href*=logout]"

    #text
    username_txt = "testdummy"
    passwd_txt = "#testdummy"


    #url
    home_url = "https://practice.automationbro.com/"
    account_url = "https://practice.automationbro.com/my-account"

    #methods
    def open_page(self):
        # open home page
            self.open(self.home_url)
    

    def login(self):
        # login
        self.open(self.account_url)
        self.add_text(self.username, self.username_txt)
        self.add_text(self.passwd,self.passwd_txt)
        self.click(self.login_btn)
        self.assert_text("Log out",".woocommerce-MyAccount-content")
       

    def logout(self):
        self.open(self.account_url)
        self.click(self.logout_btn)
        self.assert_element_visible(self.login_btn)
       