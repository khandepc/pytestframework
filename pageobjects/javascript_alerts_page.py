from generic.base import Base


linkname_javascript_alert="JavaScript Alerts"
xpath_click_for_js_alert_button="//div[@id='content']/div/ul/li/button[contains(text(),'Click for JS Alert')]"
xpath_click_for_js_conform_button="//*[@id='content']/div/ul/li[2]/button[contains(text(),'Click for JS Confirm')]"
xpath_click_for_js_prompt_button="//*[@id='content']/div/ul/li[2]/button[contains(text(),'Click for JS Prompt')]"
id_result="result"

class JavaScriptAlerts(Base):

    def get_click_for_js_alert_button_element(self):
        return self.identify_element("xpath",xpath_click_for_js_alert_button)

    def get_click_for_js_conform_button_element(self):
        return self.identify_element("xpath",xpath_click_for_js_conform_button)

    def get_click_for_js_prompt_button_element(self):
        return self.identify_element("xpath",xpath_click_for_js_prompt_button)

    def get_text_verify_element(self):
        return self.identify_element("id",id_result)

    def switch_to_alert_for_accept(self):
        return self.switch_to_another_object("alert",other="accept")

    def switch_to_alert_for_dismiss(self):
        return self.switch_to_another_object("alert",other="dismiss")

    def switch_to_alert_for_send_keys(self,value=None):
        return self.switch_to_another_object("alert",other="settext",value="accept")

    def click_on_ckick_for_js_alert_button(self):
        element=self.get_click_for_js_alert_button_element()
        self.perform_actions(element,"click")

    def verify_result_text_matching_or_not_for_js_alert_button(self):
        element=self.get_text_verify_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You successfuly clicked an alert"


    def click_on_click_for_js_conform_button(self):
        element=self.get_click_for_js_conform_button_element()
        self.perform_actions(element,"click")


    def verify_result_text_matching_or_not_for_js_conform_button_with_accept(self):
        element=self.get_text_verify_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You clicked: Ok"

    def verify_result_text_matching_or_not_for_js_conform_button_with_dismiss(self):
        element=self.get_text_verify_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You clicked: Cancel"

    def click_on_click_for_js_prompt_button(self):
        element=self.get_click_for_js_prompt_button_element()
        self.perform_actions(element,"click")
        self.switch_to_another_object("alert",other="settext",value="close with accept")

    def verify_result_text_matching_or_not_for_js_prompt_button_with_accept(self):
        element=self.get_text_verify_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You entered: close with accept"