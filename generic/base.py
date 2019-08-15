from generic.seleniumbase import SeleniumBase
from generic.apibase import ApiBase
from configparser import ConfigParser

class Base(SeleniumBase,ApiBase):

    @staticmethod
    def read_config_file(file_name,section_name):
        cp=ConfigParser()
        cp.read("./configuration/"+file_name)

        ll=cp.items(section_name)
        dd={}
        for tt in ll:
            key=tt[0]
            value=tt[1]
            dd[key]=value
        return dd



