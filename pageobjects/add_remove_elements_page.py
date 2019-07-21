from generic.base import Base


xpath_add_element="//div/button[contains(text(),'Add Element')]"
xpath_remove_element="//div/button[contains(text(),'Delete')]"

class AddRemoveElements(Base):

    def get_add_button_element(self):
        return self.identify_element("xpath",xpath_add_element)

    def click_on_add_element_button(self):
        element=self.get_add_button_element()
        self.perform_actions(element,"click")

    def get_remove_button_element(self):
        return self.identify_element("xpath",xpath_remove_element)

    def click_on_remove_button(self):
        element=self.get_remove_button_element()
        self.perform_actions(element,"click")