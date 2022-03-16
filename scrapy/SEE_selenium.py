import scrapy
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import importlib
import chrome_driver_auto
from scrapy.crawler import CrawlerProcess


############################################################################


class nameSpider(scrapy.Spider):
    name = 'name'
    start_urls = ['https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg=1']
    # def start_requests(self):
    #     yield scrapy.Request('https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg=1')
    
    custom_settings = {
        'DOWNLOAD_DELAY':1,
        'CONCURRENT_REQUESTS': 1,
        'ROBOTSTXT_OBEY' : False
    }
       
    def chrome_option():
        # re_text
        from selenium.webdriver.chrome.options import Options
        import os
        
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument(f"--window_size")
        
        # driver = webdriver.Chrome(executable_path = driver_path, chrome_options=chrome_options)
        return chrome_options
    
    global chrome_options
    chrome_options = chrome_option()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        driver_path = chrome_driver_auto.Chrome_driver.install_driver_path()
        chrome_option =chrome_options
        self.driver = webdriver.Chrome(executable_path = driver_path, chrome_options=chrome_option) 
        
    def parse(self, response):
        
        # start selenium
        self.driver.get(self.start_urls[0])
        
        # selenium movement        
        btn = self.driver.find_element_by_xpath('//*[@id="content"]/section[4]/div[2]/nav/button[2]')
        btn.click()
        time.sleep(1) 
        
        # find crawling objects
        product = response.css('li.product-grid__item')
        for item in product:
            yield{
                'name' :item.css('p.product-card__meta::text').get()
            }
    
        # # from next page
        # for x in range(2,5):
        #     yield{
        #         scrapy.Request(f'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg={x}',
        #                        callback=self.parse)
        #     }

process = CrawlerProcess(
    settings = {
        'FEEDS' : {
            'whisky.csv':{'format': 'csv'}
    }}
)

process.crawl(nameSpider)
process.start()


###https://stackoverflow.com/questions/34382356/passing-arguments-to-process-crawl-in-scrapy-python
