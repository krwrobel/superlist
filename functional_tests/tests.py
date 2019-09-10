# First function al testing with selenium

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time 
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
  
    fb = "C:\\Users\\krzysztofw\\AppData\\Local\\Mozilla Firefox\\Firefox.exe"
  
    def setUp(self):
        
        self.browser = webdriver.Firefox(firefox_binary=self.fb)

    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self, row_text):
        start_time =time.time()
        while True:
            try:
                table =self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        
    def test_can_start_a_list_and_retrive_it_latter(self):
        # Guy did heard about new to do apps, she load it to check home page
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still text box inviting him to add another item
        # He adds 'Use peacock feathers to make fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again and now shows both items on it
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make fly')

        # He is ok 

    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Guy starts a new to-do list 
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        #He noticed the unique URL
        guy_list_url = self.browser.current_url
        self.assertRegex(guy_list_url, '/lists/.+')
        
        #Later new user Frank, finds the site
        
        ## We will use new browser session to make sure 
        ## no info is coming thru cookie etc
        self.browser.quit()
        self.browser = webdriver.Firefox(firefox_binary=self.fb)
        
        #Frank visits the site. Guy list is not show
        
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        #Frank starts a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        #Frank get his own unique URL
        frank_list_url = self.browser.current_url
        self.assertRegex(frank_list_url, '/lists/.+')
        self.assertNotEqual(frank_list_url, guy_list_url)
        
        # Again ther is no trace of Guy list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        # Everything good