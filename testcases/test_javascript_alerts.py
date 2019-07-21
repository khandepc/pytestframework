from pageobjects.home_page import HomePage
from pageobjects.javascript_alerts_page import JavascriptAlerts
from generic.loggingbase import logger as log

class TestJavaScriptAlerts(HomePage,JavascriptAlerts):

    def test_verify_click_for_js_alert(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.get_home_link("JavaScript Alerts")
        self.click_on_click_for_js_alert_button()
        self.switch_to_another_object("alertaccept")
        self.verify_result_text_match_or_not()

