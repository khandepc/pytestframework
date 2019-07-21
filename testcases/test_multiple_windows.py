from pageobjects.multiple_windows_page import MultipleWindows
from pageobjects.home_page import HomePage


class TestMultipleWindows(HomePage,MultipleWindows):

    def test_switch_to_new_window(self):
        self.launch_application("chrome","https://the-internet.herokuapp.com/")
        self.click_home_link("Multiple Windows")
        self.click_click_here()
        self.switch_to_another_object("window",value="New Window")
        self.check_new_window_text()
        self.switch_to_another_object("window",value="The Internet")
        self.check_parent_window_text()
        self.close_application()
