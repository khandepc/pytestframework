from generic.base import Base

class AbTesting(Base):

    def get_AbTesting_element(self):
        return self.identify_element("linktext","A/B Testing")
