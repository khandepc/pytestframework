from pageobjects.check_box_page import CheckBoxes
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log
import pytest
class TestCheckBoxex(HomePage,CheckBoxes):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("Checkboxes")
        yield
        self.close_application()

    def test_verify_checkbox_one(self,launch_app):
        log.info("test veriry checkbox one")
        log.info("click on checkboxes link")
        self.click_on_checkbox_1()
        log.info("click on checkbox1")



