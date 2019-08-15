from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
actual_title = driver.title
expected_title = "The Internet"
assert actual_title == expected_title

xpath_js_alert_button = "//div/div/ul/li/button[contains(text(),'Click for JS Alert')]"
id_result = "result"

element = driver.find_element_by_link_text("JavaScript Alerts")
element.click()

js_alert_button = driver.find_element_by_xpath(xpath_js_alert_button)
js_alert_button.click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

actual_result_text = driver.find_element_by_id(id_result)
print(actual_result_text)
expected_text_result = "You successfuly clicked an alert"
assert actual_result_text == expected_text_result
driver.quit()