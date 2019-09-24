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
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # Home page refreshes and ther ia an error message saying that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        
        # He tries again with item which works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        #She decides to submit the empty item again
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        #Gets similar warning
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
           ))
        # He corrects it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')