from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxProfile
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

from generic.loggingbase import logger as log

class SeleniumBase:

    @staticmethod
    def launch_application(browser_name,app_url):
        global driver
        log.info("in init method of selenium base")
        try:
            if browser_name == "chrome":
                option = ChromeOptions()
                option.add_argument("start-maximized")
                option.add_argument("--ignore-certificate-errors")
                option.add_argument("--disable-extensions")
                option.add_argument("--disable-infobars")
                option.add_argument("disable-notifications")
                driver = Chrome(executable_path="./drivers/chromedriver.exe", options=option)
                log.info("chrome browser is launch successfully")
            elif browser_name == "firefox":
                profile = FirefoxProfile()
                profile.accept_untrusted_certs = True
                options = FirefoxOptions()
                options.add_argument("start-maximized")

                driver = Firefox(executable_path="./drivers/geckodriver.exe")
            elif browser_name == "ie":
                driver = Ie(executable_path="./drivers/IEDriverServer.exe")
            else:
                log.error("browser name is incorrect", browser_name)
        except WebDriverException:
            log.critical("exception", WebDriverException)

        driver.get(app_url)

    @staticmethod
    def identify_element(locater_type,address):
        if locater_type=="id":
            log.info("is selected", locater_type)
            return driver.find_element_by_id(address)
        elif locater_type=="name":
            return driver.find_element_by_name(address)
        elif locater_type=="classname":
            return driver.find_element_by_class_name(address)
        elif locater_type=="tagname":
            return driver.find_element_by_tag_name(address)
        elif locater_type=="linktext":
            return driver.find_element_by_link_text(address)
        elif locater_type=="partiallinktext":
            return driver.find_element_by_partial_link_text(address)
        elif locater_type=="css":
            return driver.find_element_by_css_selector(address)
        elif locater_type=="xpath":
            return driver.find_element_by_xpath(address)
        else:
            log.error("invalid locater type")

    @staticmethod
    def identify_elements(locater_type,address):
        log.info("is selected",locater_type)
        if locater_type == "id":
            return driver.find_elements_by_id(address)
        elif locater_type == "name":
            return driver.find_elements_by_name(address)
        elif locater_type == "classname":
            return driver.find_elements_by_class_name(address)
        elif locater_type == "tagname":
            return driver.find_elements_by_tag_name(address)
        elif locater_type == "linktext":
            return driver.find_elements_by_link_text(address)
        elif locater_type == "partiallinktext":
            return driver.find_elements_by_partial_link_text(address)
        elif locater_type == "css":
            return driver.find_elements_by_css_selector(address)
        elif locater_type == "xpath":
            return driver.find_elements_by_xpath(address)
        else:
            log.error("invalid locater type")

    @staticmethod
    def get_page_details(detail_type,element=None):
        if detail_type=="text":
            return element.text
        elif detail_type=="title":
            return driver.title
        else:
            log.error("invalid detail type")

    @staticmethod
    def wait_emplimentation(element,locater,wait_type=None,condition_type=None):
        if wait_type=="implicitewait":
            driver.implicitly_wait(20)
        elif wait_type=="explicitewait":
            wait=WebDriverWait(driver,30)
            if condition_type=="visibility":
                wait.until(ec.visibility_of_element_located(locater))

        else:
            log.error("invalid wait type")

    @staticmethod
    def perform_actions(element,action_type,value=None,other=None):
        return_value=None
        log.info("is selected",action_type,element)
        if action_type=="click":
            element.click()
        elif action_type=="settext":
            element.clear()
            element.send_keys(value)
        elif action_type=="gettext":
            return_value=element.text
        elif action_type=="getattribute":
            element.get_attribute(value)
        elif action_type=="isdisplayed":
            return_value=element.is_displayed()
        elif action_type=="isselected":
            return_value=element.is_selected()
        elif action_type=="isenabled":
            return_value=element.is_enabled()
        elif action_type=="selectdropdown":
            sel=Select(element)
            if other=="index":
                sel.select_by_index(value)
            elif other=="value":
                sel.select_by_value(value)
            elif other=="visibletext":
                sel.select_by_visible_text(value)
            elif other=="options":
                return_value=sel.options
        else:
            log.error("invalid action type")
        return return_value



    @staticmethod
    def get_screenshot(filename):
        driver.save_screenshot("./screenshots/" + filename + ".png")


    @staticmethod
    def close_application():
        log.info("application close")
        return driver.quit()

    def switch_to_another_object(self,object_type,value=None,other=None):
        return_value=None
        if object_type=="window":
            parent_handle=driver.current_window_handle
            all_handles=driver.window_handles

            for handle in all_handles:
                if handle!=parent_handle:
                    driver.switch_to.window(handle)
                    if driver.title==value:
                        break
                    else:
                        continue

        elif object_type=="frame":
            driver.switch_to.frame(value)
        elif object_type=="alert":
            alert=driver.switch_to.alert
            if other=="accept":
                alert.accept()
            elif other=="dismiss":
                alert.dismiss()
            elif other=="settext":
                alert.send_keys()
            elif other=="gettext":
                return_value=alert.text

        else:
            raise Exception
        return return_value