from generic.base import Base
from generic.loggingbase import logger as log

class TestHero(Base):
    def test_verify_total_links_on_home_page(self):
        log.info("test verify total links on home page")
        dd=self.read_config_file("base.ini","common")
        self.launch_application(dd["browser"],dd["url"])
        elements=self.identify_elements("tagname","a")
        assert len(elements)==45
        self.close_application()

    def test_verify_links_text_on_home_page(self):
        log.info("test verify links on home page")
        dd=self.read_config_file("base.ini","common")
        self.launch_application(dd["browser"],dd["url"])
        elements=self.identify_elements("xpath","//div/ul/li/a")
        assert len(elements)==43
        expected_text_list=["A/B Testing", 'Add/Remove Elements', 'Basic Auth', 'Broken Images', 'Challenging DOM',
                            'Checkboxes', 'Context Menu', 'Digest Authentication', 'Disappearing Elements', 'Drag and Drop',
                            "Dropdown", 'Dynamic Content', 'Dynamic Controls', 'Dynamic Loading', 'Entry Ad', 'Exit Intent',
                            'File Download', 'File Upload', 'Floating Menu', 'Forgot Password', 'Form Authentication', 'Frames',
                            'Geolocation', 'Horizontal Slider', 'Hovers', 'Infinite Scroll', 'Inputs', 'JQuery UI Menus',
                            'JavaScript Alerts', 'JavaScript onload event error', 'Key Presses', 'Large & Deep DOM',
                            'Multiple Windows', 'Nested Frames', 'Notification Messages', 'Redirect Link', 'Secure File Download',
                            'Shifting Content', 'Slow Resources', 'Sortable Data Tables', 'Status Codes', 'Typos',
                            'WYSIWYG Editor']

        actual_text_list=[]
        for element in elements:
            actual_text=element.text
            actual_text_list.append(actual_text)
        assert actual_text_list==expected_text_list
        self.close_application()

    def test_verify_form_authontication_invalid_credentials(self):
        log.info("test verify form authontication invalid creadentials")
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        element=self.identify_element("linktext","Form Authentication")
        element.click()
        log.info("click on",element)

        element=self.identify_element("id","username")
        element.clear()
        element.send_keys("abc")
        log.info("enter username",element)

        element=self.identify_element("id","password")
        element.clear()
        element.send_keys("SuperSecretPassword!")
        log.info("enter password",element)

        element=self.identify_element("css",".fa-sign-in")
        element.click()
        log.info("click on",element)

        expected_error_msg = "Your username is invalid!\n×"
        actual_error_msg=self.identify_element("xpath","//*[@id='flash']")
        log.info("expected error msg",expected_error_msg)
        log.info("actual error msg",actual_error_msg)
        assert actual_error_msg.text==expected_error_msg
        self.close_application()

    def test_verify_form_authontication_valid_credentials(self):
        log.info("test verify form authontication valid credentials")
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        element = self.identify_element("linktext", "Form Authentication")
        element.click()
        log.info("click on",element)

        element=self.identify_element("id","username")
        element.clear()
        element.send_keys("tomsmith")
        log.info("enter user name",element)

        element=self.identify_element("id","password")
        element.clear()
        element.send_keys("SuperSecretPassword!")
        log.info("enter password",element)

        element=self.identify_element("css",".fa-sign-in")
        element.click()
        log.info("click on",element)
        self.close_application()

    def test_verify_check_boxes_credentials(self):
        log.info("test verify check boxes credentials")
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        element=self.identify_element("linktext","Checkboxes")
        element.click()
        log.info("click on",element)

        element=self.identify_element("xpath","//div/div/form/input[1]")
        status=element.is_selected()
        if status==False:
            element.click()
        log.info("select",element)
        self.close_application()

