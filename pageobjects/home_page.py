from generic.base import Base

linktextHomeLink='{}'

class HomePage(Base):

    def get_home_link(self,linkname):

        return self.identify_element("linktext",linktextHomeLink.format(linkname))


    def click_home_link(self,linkname):
        element=self.get_home_link(linkname)
        self.perform_actions(element=element,action_type="click")