from pageobjects.dropdown_page import DropDown
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log


class TestDropDown(HomePage,DropDown):


    def test_verify_count_of_options(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        option_list=self.perform_actions(element,"selectdropdown",other="options")
        log.info("verify options are matching with count of 3")
        assert len(option_list)==3
        self.close_application()

    def test_verify_select_option_one_by_index(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown",1,"index")
        log.info("select option one by index")
        self.close_application()

    def test_verify_select_option_one_by_value(self):
        self.launch_application("chrome", "https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","1","value")
        log.info("select option one by value")
        self.close_application()

    def test_verify_select_option_one_by_visible_text(self):
        self.launch_application("chrome", "https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","Option 1","visibletext")
        log.info("select option one by visibletext")
        self.close_application()

    def test_verify_select_option_two_by_index(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown",2,"index")
        log.info("select option two by index")
        self.close_application()

    def test_verify_select_option_two_by_value(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","2","value")
        log.info("select option two by value")
        self.close_application()

    def test_verify_select_option_two_by_visible_text(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Dropdown")
        element=self.get_drop_down_element()
        element=self.perform_actions(element,"selectdropdown","Option 2","visibletext")
        log.info("select option two by visibletext")

        self.close_application()





