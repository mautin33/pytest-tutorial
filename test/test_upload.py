from page_objects.upload_page import UploadPage

class UploadTest(UploadPage):

    def test_visible_upload(self):
        # open page
        self.open_page()

        # upload file
        self.choose_file(self.fileUpload_1,self.filePath)

        # click the upload button
        self.click(self.upload_btn)

        # assert file uploaded text
        self.assert_text("File Uploaded", "h3")
        


    def test_hidden_upload(self):
        # open page
        self.open_page_2()
       
        # add js code
        remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)
        
        # upload file
        self.choose_file(self.fileUpload_2,self.filePath)

        # click the upload button
        self.click(self.upload_btn_2)

        # assert file uploaded text
        self.assert_text("uploaded successfully", self.uploadMessage)

                                                                                                                                                                                                                        

