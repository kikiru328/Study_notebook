import scrapy
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append('../../')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import importlib

class XSpider(scrapy.Spider):
    name = 'x'
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        passpy = self.passpy
        passing = importlib.import_module(passpy)
        selenium_start_url = passing.urls()
        
        driver_path = passing.Chrome_driver.install_driver_path()
        chrome_options = passing.Chrome_driver.chrome_option()
        self.driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
        self.driver.get(selenium_start_url[0])

        # selenium movement
        passing.selenium_movement(self)
        self.driver.close()
    
    # allowed_domains = ['x']
    # start_urls = ['http://x/']

    def parse(self, response):
        time.sleep(2)
        passing = importlib.import_module(self.passpy)
        
        # selenium crawling
        passing.selenium_crawling(response)
        
        
        # pass

