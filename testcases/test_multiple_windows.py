from pageobjects.multiple_windows_page import MultipleWindows
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log
import pytest

class TestMultipleWindows(HomePage,MultipleWindows):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("Multiple Windows")
        yield
        self.close_application()

    def test_switch_to_new_window(self,launch_app):
        log.info("test switch to new window")
        self.click_click_here()
        self.switch_to_another_object("window",value="New Window")
        self.check_new_window_text()
        self.switch_to_another_object("window",value="The Internet")
        self.check_parent_window_text()
