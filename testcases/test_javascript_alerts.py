from pageobjects.home_page import HomePage
from pageobjects.javascript_alerts_page import JavaScriptAlerts
import pytest

class TestJavascriptAlerts(HomePage,JavaScriptAlerts):

    @pytest.fixture()
    def launch_app(self):
        dd = self.read_config_file("base.ini","common")
        self.launch_application(dd["browser"], dd["url"])
        self.click_home_link("JavaScript Alerts")

    def test_verify_functionality_of_javascript_alerts_button(self,launch_app):

        self.click_on_ckick_for_js_alert_button()
        self.switch_to_alert_for_accept()
        self.verify_result_text_matching_or_not_for_js_alert_button()
        self.close_application()

    def test_verify_functionality_of_click_for_js_conform_button_with_accept(self,launch_app):

        self.click_on_click_for_js_conform_button()
        self.switch_to_alert_for_accept()
        self.verify_result_text_matching_or_not_for_js_conform_button_with_accept()
        self.close_application()

    def test_verify_functionality_of_click_for_js_conform_button_with_dismiss(self,launch_app):

        self.click_on_click_for_js_conform_button()
        self.switch_to_alert_for_dismiss()
        self.verify_result_text_matching_or_not_for_js_conform_button_with_dismiss()
        self.close_application()

    def test_verify_functionality_of_click_for_js_prompt_button(self,launch_app):

        self.click_on_click_for_js_prompt_button()
        self.switch_to_alert_for_accept()
        self.verify_result_text_matching_or_not_for_js_prompt_button_with_accept()
        self.close_application()

