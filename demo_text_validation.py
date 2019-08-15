from selenium import webdriver
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

user_name="tomsmith"
password="SuperSecretPassword!"
id_user_name_input_box="username"
id_password_input_box="password"
xpath_login_button="//form[@id='login']/button[@class='radius']"
id_login_result="flash"
element=driver.find_element_by_link_text("Form Authentication")
element.click()
element=driver.find_element_by_id(id_user_name_input_box)
element.send_keys(user_name)
element=driver.find_element_by_id(id_password_input_box)
element.send_keys(password)
element=driver.find_element_by_xpath(xpath_login_button)
element.click()
element=driver.find_element_by_id(id_login_result)
actual_text=element.text
assert actual_text=="You logged into a secure area!\n×"
driver.close()