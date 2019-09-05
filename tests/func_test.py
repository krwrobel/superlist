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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feather" into a text box
        inputbox.send_keys('Buy peacock feathers')
        
        # When hiting enter the page ypdtes and now the page looks like:
        # 1: Buy peackock feathers as a an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peackock feathers' for row in rows)
            )
        # There is still text box inviting her to add another item
        # He adds 'Use peacock feathers to make fly'
        self.fail('Finish the test')
        
        # The page updates again and now shows both items on it

        # Edith wonders whather the site will remember her list. she notice about
        # generated a unique URL for her 

        # He visits the URL - her to-do list is still there

        # He is ok 

if __name__ == '__main__':
        unittest.main(warnings='ignore')