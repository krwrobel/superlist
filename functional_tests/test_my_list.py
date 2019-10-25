from django.conf import settings
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session
from .base import FunctionalTest

class MyListsTest(FunctionalTest):
    
    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## to set cookie we need visit the domain
        ## 404 pages load the quickest!
        
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))
        
    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        #Usrer is logged in
        self.create_pre_authenticated_session('edith@example.com')
        
        #User starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulate splines')
        self.add_list_item('Ammanentize eschaton')
        
        first_list_url = self.browser.current_url
        
        # He see the "My lists" link
        self.browser.find_element_by_link_text('My lists').click()
        
        # He see the list named according to first item
        self.wait_for( 
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
            )
        self.browser.find_element_by_link_text('Reticulate splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
            )
            
        # User adds another list
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url
        
        #Under "my list" appears:
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )
        
        #She logs out. The 'My lists' option disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))
        
        
            