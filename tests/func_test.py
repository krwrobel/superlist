from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#cap = DesiredCapabilities().FIREFOX
fb = "C:\\Users\\krzysztofw\\AppData\\Local\\Mozilla Firefox\\Firefox.exe"
#ep = "C:\\dev\\geckodriver-v0.24.0-win64\\geckodriver.exe"
#browser = webdriver.Firefox(capabilities=cap,firefox_binary=fb, executable_path=ep)
browser = webdriver.Firefox(firefox_binary=fb)
browser.get('http://localhost:8000')

assert 'Django' in browser.title