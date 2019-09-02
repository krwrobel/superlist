# First function al testing with selenium

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        fb = "C:\\Users\\krzysztofw\\AppData\\Local\\Mozilla Firefox\\Firefox.exe"
        self.browser = webdriver.Firefox(firefox_binary=fb)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_latter(self):
        # Guy did heard about new to do apps, she load it to check home page
        self.browser.get('http://localhost:8000')

        #He noticed the page tile and header 
        self.assertIn( 'To-Do',self.browser.title)
        self.fail('End of test')

        #He is invited to enter a to-do item straight away

        # He types "Buy pwacock feather" into a text box

        # When hiting enter the page ypdtes and now the page looks like:
        # 1: Buy peackock feathers as a an item in a to-do list

        # Ther is still text box inviting her to add andother item
        # He  adds 'Use peacock feathers to maje fly

        # The page updates again and now shows both items on it

        # Edith wonders whather the site will remember her list. she notice about
        # generated a unique URL for her 

        # He visits the URL - her to-do list is still there

        # He is ok 

if __name__ == '__main__':
        unittest.main(warnings='ignore')