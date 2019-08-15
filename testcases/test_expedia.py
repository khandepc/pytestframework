import time
from generic.seleniumbase import SeleniumBase
from selenium.webdriver.support.wait import WebDriverWait

xpath_flight_button = "//div/ul/li/button[@id='tab-flight-tab-hp']"
id_return_button = "flight-type-roundtrip-label-hp-flight"
id_flying_from_input_box = "input#flight-origin-hp-flight"
xpath_pune="//span/div[@class='multiLineDisplay']/b[contains(text(),'Pune')]"
id_flying_to_input_box = "input#flight-destination-hp-flight"
xpath_mumbai="//span/div[@class='multiLineDisplay']/b[contains(text(),'Mumbai')]"
id_departing_input_box = "input#flight-departing-hp-flight"
id_returning_input_box = "input#flight-returning-hp-flight"
xpath_search_button = "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button/span"

class TestExpedia:
    def test_functionality_of_expedia_with_valid_detail(self):
        sb=SeleniumBase("chrome")
        sb.launch_application("https://www.expedia.co.in/")
        expected_title="Expedia Travel: Vacations, Cheap Flights, Airline Tickets & Airfares"
        actual_title=sb.get_page_details("title")
        assert actual_title==expected_title


        element=sb.identify_element("xpath",xpath_flight_button)
        element.click()

        element=sb.identify_element("id",id_return_button)
        element.click()

        element=sb.identify_element("css",id_flying_from_input_box)
        element.clear()
        element.send_keys("Pune")



        element=sb.identify_element("css",id_flying_to_input_box)
        element.clear()
        element.send_keys("Mumbai")

        element=sb.identify_element("css",id_departing_input_box)
        element.clear()
        element.send_keys("10/07/2019")

        element=sb.identify_element("css",id_returning_input_box)
        element.click()
        element.clear()
        element.send_keys("12/07/2019")
        import pdb
        pdb.set_trace()

        element=sb.identify_element("xpath",xpath_search_button)
        element.click()

        sb.close_application()
