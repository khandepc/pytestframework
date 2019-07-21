from pageobjects.check_box_page import CheckBoxes
from pageobjects.home_page import HomePage
from generic.loggingbase import logger as log

class TestCheckBoxex(HomePage,CheckBoxes):

    def test_verify_checkbox_one(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Checkboxes")
        log.info("click on checkboxes link")
        self.click_on_checkbox_1()
        log.info("click on checkbox1")
        self.close_application()

        self.switch_to_another_object("alert","accept")

