from pageobjects.home_page import HomePage
from pageobjects.form_authontication_page import FormAuthontication
import pytest

class TestFormAuthontication(HomePage,FormAuthontication):

    @pytest.fixture()
    def launch_app(self):
        dd=self.read_config_file("base.ini", "common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("Form Authentication")
        yield
        self.close_application()

    def test_form_authontication_page_with_valid_details(self,launch_app):
        self.enter_valid_user_name_as_tomsmith()
        self.enter_valid_password_as_SuperSecretPassword()
        self.click_on_login_button()
        self.verify_login_result_text()
        self.click_on_logout_button()
        self.verify_logout_result_text()

    def test_form_authontication_page_with_invalid_details_username_as_prashant(self,launch_app):
        self.enter_invalid_user_name_as_prashant()
        self.enter_valid_password_as_SuperSecretPassword()
        self.click_on_login_button()
        self.verify_log_in_error_of_user_name_prashant()
