# First function al testing with selenium

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


MAX_WAIT = 10

class ItemValidationTest(FunctionalTest):
        
    def test_cannot_add_empty_list_items(self):
        #Customer goes to home page and acciedentally tries to submit
        # a empty list item. Hits Enter on empty input box

        # Home page refreshes and ther ia an error message saying that list items cannot be blank
        
        # He tries again with item which works
        
        #She decides to submit the empty item again
        
        #Gets similar warning
        
        # He corrects it by filling some text in
