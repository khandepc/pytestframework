from generic.base import Base
from generic.loggingbase import logger as log

linktextHomeLink='{}'

class HomePage(Base):

    def get_home_link(self,linkname):

        return self.identify_element("linktext",linktextHomeLink.format(linkname))


    def click_home_link(self,linkname):
        log.info("click on homelink", linkname)
        elem=self.get_home_link(linkname)
        self.perform_actions(element=elem,action_type="click")

