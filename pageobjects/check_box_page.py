from generic.base import Base
from generic.loggingbase import logger as log


xpath_checkbox_1="//form/input[1]"
xpath_checkbox_2="//form/input[2]"

class CheckBoxes(Base):

    def get_checkbox_1_element(self):
        return self.identify_element("xpath",xpath_checkbox_1)

    def click_on_checkbox_1(self):
        element=self.get_checkbox_1_element()
        if element.is_selected()==False:
            self.perform_actions(element,"click")
        else:
            log.error("checkbox already selected",element.is_selected())



