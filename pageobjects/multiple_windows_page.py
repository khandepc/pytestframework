from generic.base import Base

linktext_click_here="Click Here"
xpath_new_window_text="//div[@class='example']"
xpath_parent_window_text="//div/div/h3"

class MultipleWindows(Base):

    def get_click_here_element(self):
        return self.identify_element("linktext",linktext_click_here)

    def click_click_here(self):
        element=self.get_click_here_element()
        self.perform_actions(element,action_type="click")

    def get_new_window_text_element(self):
        return self.identify_element("xpath",xpath_new_window_text)

    def check_new_window_text(self):
        element=self.get_new_window_text_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="New Window"

    def get_parent_window_text_element(self):
        return self.identify_element("xpath",xpath_parent_window_text)

    def check_parent_window_text(self):
        element=self.get_parent_window_text_element()
        actual_text=self.perform_actions(element,"gettext")
        assert actual_text=="Opening a new window"
