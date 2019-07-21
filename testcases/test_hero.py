from generic.seleniumbase import SeleniumBase
from generic.loggingbase import logger as log
class TestHero:
    def test_verify_total_links_on_home_page(self):
        sb=SeleniumBase("chrome")
        sb.launch_application("https://the-internet.herokuapp.com/")
        elements=sb.identify_elements("tagname","a")
        assert len(elements)==45
        sb.close_application()

    def test_verify_links_text_on_home_page(self):

        sb=SeleniumBase("chrome")
        sb.launch_application("https://the-internet.herokuapp.com/")
        elements=sb.identify_elements("xpath","//div/ul/li/a")
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

        #import pdb
        #pdb.set_trace()
        sb.close_application()

    def test_verify_form_authontication_invalid_credentials(self):
        sb=SeleniumBase("chrome")
        sb.launch_application("https://the-internet.herokuapp.com/")

        element=sb.identify_element("linktext","Form Authentication")
        element.click()
        log.info("click on",element)


        element=sb.identify_element("id","username")
        element.clear()
        element.send_keys("abc")
        log.info("enter username",element)

        element=sb.identify_element("id","password")
        element.clear()
        element.send_keys("SuperSecretPassword!")
        log.info("enter password",element)

        element=sb.identify_element("css",".fa-sign-in")
        element.click()
        log.info("click on",element)

        expected_error_msg = "Your username is invalid!\n×"
        actual_error_msg=sb.identify_element("xpath","//*[@id='flash']")
        log.info("expected error msg",expected_error_msg)
        log.info("actual error msg",actual_error_msg)

        assert actual_error_msg.text==expected_error_msg

        sb.close_application()



    def test_verify_form_authontication_valid_credentials(self):
        sb = SeleniumBase("chrome")
        sb.launch_application("https://the-internet.herokuapp.com/")

        element = sb.identify_element("linktext", "Form Authentication")
        element.click()
        log.info("click on",element)


        element=sb.identify_element("id","username")
        element.clear()
        element.send_keys("tomsmith")
        log.info("enter user name",element)

        element=sb.identify_element("id","password")
        element.clear()
        element.send_keys("SuperSecretPassword!")
        log.info("enter password",element)

        element=sb.identify_element("css",".fa-sign-in")
        element.click()
        log.info("click on",element)

    def test_verify_check_boxes_credentials(self):
        sb=SeleniumBase("chrome")
        sb.launch_application("https://the-internet.herokuapp.com/")

        element=sb.identify_element("linktext","Checkboxes")
        element.click()
        log.info("click on",element)

        element=sb.identify_element("xpath","//div/div/form/input[1]")
        status=element.is_selected()
        if status==False:
            element.click()
        log.info("select",element)

