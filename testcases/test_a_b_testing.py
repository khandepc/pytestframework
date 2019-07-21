from pageobjects.a_b_testing_page import AbTesting
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log


class TestAbTesting(HomePage,AbTesting):

    def test_verify_count_of_options(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("A/B Testing")
        log.info("click on Abtesting link")

