from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
actual_title=driver.title
expected_title="The Internet"
assert actual_title==expected_title


element=driver.find_element_by_link_text("JavaScript Alerts")
element.click()
xpath_js_prompt_button="//div/div/ul/li[3]/button[contains(text(),'Click for JS Prompt')]"
element=driver.find_element_by_xpath(xpath_js_prompt_button)
element.click()
alert=driver.switch_to.alert
alert.send_keys("close with accept")
alert.accept()
id_result="result"
element=driver.find_element_by_id(id_result)
actual_text=element.text
expected_text="You entered: close with accept"
assert actual_text==expected_text

driver.close()