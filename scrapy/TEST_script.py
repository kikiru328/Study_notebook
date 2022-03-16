# import module
import scrapy
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import warnings
warnings.filterwarnings("ignore")
import time
import chrome_driver_auto
driver_path = chrome_driver_auto.Chrome_driver.install_driver_path()
chrome_option = chrome_driver_auto.Chrome_driver.chrome_option()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from scrapy.crawler import CrawlerProcess

# Start Cralwing
class testSpider(scrapy.Spider):
    
    # testSpider  == calling name
    name = 'test'
    
    # the First url
    def start_requests(self):
        yield scrapy.Request('https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg=1')
        
    def parse(self, response):
        product = response.css('li.product-grid__item')
        for item in product:
            yield{
                'name' :item.css('p.product-card__meta::text').get()
            }
    
        # from next page
        for x in range(2,5):
            yield{
                scrapy.Request(f'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg={x}',
                               callback=self.parse)
            }

process = CrawlerProcess(
    settings = {
        'FEEDS' : {
            'whisky.csv':{'format': 'csv'}
    }}
)

process.crawl(testSpider)
process.start()
