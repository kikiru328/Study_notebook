import scrapy
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append('../')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import chrome_driver_auto
import importlib

# def getmodule(self):
#     global passing
#     passing = importlib.import_module(self.file)
#     return passing

class NameSpider(scrapy.Spider):
    name = 'name'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']
    def get_module(self):
        global passing
        passing = importlib.import_module(self.import_module)
        return passing
    
    def start(self):
        # file = self.file
        # import importlib
        # passing = importlib.import_module(self.file)
        
        driver_path = chrome_driver_auto.Chrome_driver.install_driver_path()
        chrome_option = chrome_driver_auto.Chrome_driver.chrome_option()
        
        # driver_path = passing.driver_path
        # chrome_option = passing.driver_option
        driver = webdriver.Chrome(executable_path = driver_path, chrome_options=chrome_option)
        self.driver = driver
        # return self.driver
        
        # url = passing.crawling.url()
        # driver.get(url)
        
        # elements = passing.selenium_movement(driver_path,chrome_option)
            
        # for element in elements:
        #     href = element.get_attribute('href')
        #     yield scrapy.Request(href)
        
    def parse(self, response):
        import importlib
        passing = importlib.import_module(self.file)
        url = passing.crawling.url()
        self.driver.get(url)
        btn = self.driver.find_element_by_title('Next Page')
        btn.click()
        time.sleep(1)
        product = response.css('li.product-grid__item')
        for item in product:
            yield {
                'proof' : item.css('p.product-card__meta::text').get()
            }
        self.driver.close()
        
        # pass
        