from pageobjects.dropdown_page import DropDown
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log
import pytest

class TestDropDown(HomePage,DropDown):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("Dropdown")
        yield
        self.close_application()


    def test_verify_count_of_options(self,launch_app):
        log.info("test verify count of options")

        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        option_list=self.perform_actions(element,"selectdropdown",other="options")
        log.info("verify options are matching with count of 3")
        assert len(option_list)==3

    def test_verify_select_option_one_by_index(self,launch_app):
        log.info("test verify select option one by index")
        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown",1,"index")
        log.info("select option one by index")

    def test_verify_select_option_one_by_value(self,launch_app):
        log.info("test verify select option one by value")
        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","1","value")
        log.info("select option one by value")

    def test_verify_select_option_one_by_visible_text(self,launch_app):
        log.info("test verify select option one by visible text")

        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","Option 1","visibletext")
        log.info("select option one by visibletext")

    def test_verify_select_option_two_by_index(self,launch_app):
        log.info("test verify select option two by index")
        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown",2,"index")
        log.info("select option two by index")

    def test_verify_select_option_two_by_value(self,launch_app):
        log.info("test verify select option two by value")
        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","2","value")
        log.info("select option two by value")

    def test_verify_select_option_two_by_visible_text(self,launch_app):
        log.info("test verify select option two by visible text")
        log.info("click on home link dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","Option 2","visibletext")
        log.info("select option two by visibletext")





