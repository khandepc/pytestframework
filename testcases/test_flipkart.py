
from generic.seleniumbase import SeleniumBase

class TestFlipkart:

    def test_total_count_of_img_on_flipkart_home_page(self):
        sb=SeleniumBase("chrome")
        sb.launch_application("https://www.flipkart.com")
        element=sb.identify_element("xpath","/html/body/div[2]/div/div/button")
        element.click()
        elements=sb.identify_elements("tagname","img")
        assert len(elements)==51

        actual_texts_list=[]
        sb.close_application()
