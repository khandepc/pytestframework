from pageobjects.add_remove_elements_page import AddRemoveElements
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log
import pytest
class TestAddRemoveElements(HomePage,AddRemoveElements):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("Add/Remove Elements")
        yield
        self.close_application()

    def test_verify_count_of_options(self,launch_app):
        log.info("verify count of options")
        log.info("click on Add/remove elements link")
        self.click_on_add_element_button()
        log.info("click on add element button")
        self.click_on_remove_button()
        log.info("click on remove element button")
