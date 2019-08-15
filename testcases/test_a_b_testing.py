from pageobjects.a_b_testing_page import AbTesting
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log
import pytest

class TestAbTesting(HomePage,AbTesting):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("A/B Testing")
        yield
        self.close_application()

    def test_verify_count_of_options(self,launch_app):
        log.info("test verify count of options")
        log.info("click on Abtesting link")

