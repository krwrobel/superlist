# First function al testing with selenium

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        #Customer goes to home page and acciedentally tries to submit
        # a empty list item. Hits Enter on empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        #Browser dont let the site reload
        self.wait_for(lambda:
            self.browser.find_element_by_css_selector('#id_text:invalid')   
        )
        
        # He tries again with item which works
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda:
            self.browser.find_element_by_css_selector('#id_text:valid')   
        )
        
        #He is able to submit it
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        #She decides to submit the empty item again
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        #Browser dont budge
        self.wait_for(lambda:
            self.browser.find_element_by_css_selector('#id_text:invalid')   
        )
        
        # He corrects it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda:
            self.browser.find_element_by_css_selector('#id_text:valid')   
        )        
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')