from selenium import webdriver

driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
actual_title = driver.title
expected_title = "The Internet"
assert actual_title == expected_title
xpath_js_conform_button = "//div[@class='example']/ul/li[2]/button"
id_result = "result"

element = driver.find_element_by_link_text("JavaScript Alerts")
element.click()

js_conform_button = driver.find_element_by_xpath(xpath_js_conform_button)
js_conform_button.click()
alert = driver.switch_to.alert
alert.accept()

actual_result_text = driver.find_element_by_id(id_result)
expected_result_text = "You clicked: Ok"
assert actual_result_text == expected_result_text
driver.close()
