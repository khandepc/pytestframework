from generic.base import Base

user_name="tomsmith"
password="SuperSecretPassword!"
id_user_name_input_box="username"
id_password_input_box="password"
xpath_login_button="//form[@id='login']/button[@class='radius']"
xpath_login_result="//div[@class='row']/div[@id='flash-messages']/div[@id='flash']"
xpath_logout_button="//div[@id='content']/div[@class='example']/a"
xpath_logout_result_text="//div[@id='flash']"

class FormAuthontication(Base):

    def get_user_name_input_box_element(self):
        return self.identify_element("id",id_user_name_input_box)

    def get_password_input_box_element(self):
        return self.identify_element("id",id_password_input_box)

    def get_login_button_element(self):
        return self.identify_element("xpath",xpath_login_button)

    def get_text_result_of_login_element(self):
        return self.identify_element("xpath",xpath_login_result)

    def get_logout_button_element(self):
        return self.identify_element("xpath",xpath_logout_button)

    def get_logout_text_element(self):
        return self.identify_element("xpath",xpath_logout_result_text)

    def enter_valid_user_name_as_tomsmith(self):
        element=self.get_user_name_input_box_element()
        self.perform_actions(element,"settext",value=user_name)

    def enter_valid_password_as_SuperSecretPassword(self):
        element=self.get_password_input_box_element()
        self.perform_actions(element,"settext",value=password)

    def click_on_login_button(self):
        element=self.get_login_button_element()
        self.perform_actions(element,"click")

    def verify_login_result_text(self):
        element=self.get_text_result_of_login_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You logged into a secure area!\n×"

    def click_on_logout_button(self):
        element=self.get_logout_button_element()
        self.perform_actions(element,"click")

    def verify_logout_result_text(self):
        element=self.get_logout_text_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="You logged out of the secure area!\n×"

    def enter_invalid_user_name_as_prashant(self):
        element=self.get_user_name_input_box_element()
        self.perform_actions(element,"settext",value="Prashant")


    def verify_log_in_error_of_user_name_prashant(self):
        element=self.get_text_result_of_login_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="Your username is invalid!\n×"