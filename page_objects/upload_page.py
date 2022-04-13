from seleniumbase import BaseCase

class UploadPage(BaseCase):
    # selectors 
    filePath = "./data/img.png" #file path
    fileUpload_1 = "#file-upload" 
    upload_btn = '#file-submit'

    fileUpload_2 = "#upfile_1" 
    upload_btn_2 = "#upload_1"
    uploadMessage = "#wfu_messageblock_header_1_label_1"

    # text

    # url
    heroku_url = "https://the-internet.herokuapp.com/upload"
    automationbro_url = "https://practice.automationbro.com/cart"

    # methods
    def open_page(self):
        # open page
        self.open(self.heroku_url)

    def open_page_2(self):
        # open page
        self.open(self.automationbro_url )