from seleniumbase import BaseCase

class ContactPage(BaseCase):
    # selectors
    contact_name = '.contact-name input'
    contact_email = '.contact-email input'
    contact_phoneNo = '.contact-phone input'
    contact_message = '.contact-message textarea'
    submit_btn = "#evf-submit-277"
    verification_message = "div[role=alert]"
    contact_form = "#evf-form-277"
    
    # text
    contact_name_txt = 'Test Name'
    contact_email_txt = 'test@gmail.com'
    contact_phoneNo_txt = '123456789'
    contact_message_txt = 'This is a text message'
    verification_message_txt = "Thanks for contacting us! We will be in touch with you shortly"

    def openPage(self):
        # open page
        url = "https://practice.automationbro.com/contact/"
        self.open(url)