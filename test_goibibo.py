from generic.seleniumbase import SeleniumBase as sb


sb.launch_application('chrome', "https://www.goibibo.com/")

element = sb.identify_element('id','gosuggest_inputSrc')
sb.perform_actions(element, 'settext', "Pune (PNQ)")
sb.key_operations(element, 'down')
sb.key_operations(element, 'enter')
sb.perform_actions(element,'click')
sb.key_operations(element, 'tab')
element = sb.identify_element('id','gosuggest_inputDest')
sb.perform_actions(element, 'settext', "Mumbai (BOM)")
sb.key_operations(element, 'down')
sb.key_operations(element, 'enter')
sb.perform_actions(element,'click')
sb.key_operations(element, 'tab')

#sb.perform_actions(None, 'setattribute', "Tue, 30 Jul", "input[placeholder='Departure']")
#sb.close_application()

