from pageobjects.add_remove_elements_page import AddRemoveElements
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log

class TestAddRemoveElements(HomePage,AddRemoveElements):

    def test_verify_count_of_options(self):
        log.info("verify count of options")
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Add/Remove Elements")
        log.info("click on Add/remove elements link")
        self.click_on_add_element_button()
        log.info("click on add element button")
        self.click_on_remove_button()
        log.info("click on remove element button")
        self.close_application()