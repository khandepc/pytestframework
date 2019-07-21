from generic.base import Base

xpath_click_for_js_alert_button="//ul/li/button[contains(text(),'Click for JS Alert')]"
xpath_click_for_js_conform_button="//div/ul/li/button[contains(text(),'Click for JS Confirm')]"
xpath_click_for_js_prompt="//div/ul/li/button[contains(text(),'Click for JS Prompt')]"
id_result="result"

class JavascriptAlerts(Base):

    def get_click_for_js_alert_button_element(self):
        return self.identify_element("xpath",xpath_click_for_js_alert_button)

    def click_on_click_for_js_alert_button(self):
        element=self.get_click_for_js_alert_button_element()
        self.perform_actions(element,"click")

    def get_result_text_element(self):
        return self.identify_element("id",id_result)

    def verify_result_text_match_or_not(self):
        element=self.get_result_text_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You successfuly clicked an alert"