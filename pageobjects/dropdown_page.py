from generic.base import Base


id_drop_down="dropdown"
visible_text_option_one="Option 1"
visible_text_option_two="Option 2"
value_option_one="1"
value_option_two="2"

class DropDown(Base):

    def get_drop_down_element(self):
        return self.identify_element("id",id_drop_down)
