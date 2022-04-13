from page_objects.contact_page import ContactPage

class ContactTest(ContactPage):
    def setUp(self):
        super().setUp()

        self.openPage()

    def test_contact_page(self):

        # scroll to the empty form and take screenshot
        self.scroll_to(ContactPage.contact_form)
        self.save_screenshot("empty_contact_form","custom_screenshots")

        # fill in all the fields
        self.send_keys(ContactPage.contact_name, ContactPage.contact_name_txt)
        self.send_keys(ContactPage.contact_email, ContactPage.contact_email_txt)
        self.send_keys(ContactPage.contact_phoneNo, ContactPage.contact_phoneNo_txt)
        self.send_keys(ContactPage.contact_message, ContactPage.contact_message_txt)

        # scroll to when form is filled
        self.scroll_to(ContactPage.contact_form)
        self.save_screenshot("filled_contact_form","custom_screenshots")

        # click the submit button
        self.click(ContactPage.submit_btn)

        # verify submit message
        self.assert_text(ContactPage.verification_message_txt,ContactPage.verification_message)

        # 
        self.post_message("PASSED")