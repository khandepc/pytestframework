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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
                log.info("firefox browser is launch successfully")
            elif browser_name == "ie":
                driver = Ie(executable_path="./drivers/IEDriverServer.exe")
            else:
                log.error("browser name is incorrect", browser_name)
        except WebDriverException:
            log.critical("exception", WebDriverException)
        driver.implicitly_wait(5)
        driver.get(app_url)

    @staticmethod
    def identify_element(locater_type,address):
        element=None
        wait=WebDriverWait(driver,20,1)
        if locater_type=="id":
            locater=By.ID,address
            condition=ec.presence_of_element_located(locater)
            element=wait.until(condition)
            return element
        elif locater_type=="name":
            locater = By.NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="classname":
            locater = By.CLASS_NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="tagname":
            locater = By.TAG_NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="linktext":
            locater = By.LINK_TEXT, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="partiallinktext":
            locater = By.PARTIAL_LINK_TEXT, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="css":
            locater = By.CSS_SELECTOR, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="xpath":
            locater = By.XPATH, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        else:
            log.error("invalid locater type")

    @staticmethod
    def identify_elements(locater_type,address):
        element=None
        wait=WebDriverWait(driver,20,1)
        if locater_type == "id":
            locater = By.ID, address
            condition=ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "name":
            locater = By.NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "classname":
            locater = By.CLASS_NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "tagname":
            locater = By.TAG_NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "linktext":
            locater = By.LINK_TEXT, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "partiallinktext":
            locater = By.PARTIAL_LINK_TEXT, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "css":
            locater = By.CSS_SELECTOR, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "xpath":
            locater = By.XPATH, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        else:
            log.error("invalid locater type")

    @staticmethod
    def get_page_details(detail_type,element=None):
        if detail_type=="text":
            return element.text
        elif detail_type=="title":
            return driver.title
        elif detail_type=="url":
            return driver.current_url
        else:
            log.error("invalid detail type")


    @staticmethod
    def key_operations(element, action_type):
        if action_type == 'down':
            element.send_keys(Keys.ARROW_DOWN)
        elif action_type == 'enter':
            element.send_keys(Keys.ENTER)
        elif action_type == 'tab':
            element.send_keys(Keys.TAB)

    @staticmethod
    def wait_emplimentation(element,wait_type):
        element=None
        if wait_type=="implicitewait":
            driver.implicitly_wait(20)
        elif wait_type=="explicitewait":
            wait=WebDriverWait(driver,30)
            wait.until(ec.visibility_of_element_located(element))
            return element
        else:
            log.error("invalid wait type")

    @staticmethod()
    def perform_actions(element,action_type,value=None,other=None):
        return_value=None
        if action_type=="click":
            element.click()
        elif action_type=="settext":
            element.clear()
            element.send_keys(value)
        elif action_type=="gettext":
            return_value=element.text
        elif action_type=="getattribute":
            element.get_attribute(value)
        elif action_type == 'setattribute':
            script = "document.getElementsByClassName('"+other+"')[0].value = "+value+")"
            driver.execute_script(script)
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
    def capture_screenshot(filename):
        driver.save_screenshot("./screenshots/"+filename+".png")



    def close_application(self):
        #self.capture_screenshot(filename=None)
        log.info("application close")
        driver.quit()

    def switch_to_another_object(self,object_type,value=None,other=None):
        log.info("switch to window")
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
                alert.send_keys(value)
            elif other=="gettext":
                return_value=alert.text
        else:
            raise Exception
        return return_value

    @staticmethod
    def perform_mouse_keyboard_actions(element,action_type,source_element=None,dest_element=None,value=None):
            ac=ActionChains(driver)
            if action_type=="rightclick":
                ac.context_click(element)
            elif action_type=="movetoelement":
                ac.move_to_element(element)
            elif action_type=="click":
                ac.click(element)
            elif action_type=="sendkeys":
                ac.send_keys(value)
            elif action_type=="draganddrop":
                ac.drag_and_drop(source_element,dest_element)
            elif action_type=="doubleclick":
                ac.double_click(element)
            elif action_type=="clickandhold":
                ac.click_and_hold(element)
            elif action_type=="keydown":
                ac.key_down(value,element)
            elif action_type=="keyup":
                ac.key_up(value,element)
            else:
                print("invalid action type")
            ac.perform()
