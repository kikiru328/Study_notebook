import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import warnings
warnings.filterwarnings("ignore")
import time

from urllib import request
from time import sleep, time
import os
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
import shutil

class crawl_form:
    def url():
        url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=190991'
        return url

    def parse(response):
        visitors = response.css('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(10) > div > p.count::text').get()
        print(f'관객수 > {visitors}')
        # l = ItemLoader(item = MovieItem(), selector=response)
        # l.add_css('관객수','p.count::text')
        # yield l.load_item()

class active_crawl:   
    
    # global chrome_driver_selenium
    def chrome_driver_selenium():
        import shutil
        import chromedriver_autoinstaller
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        driver_path = f'{chrome_version}\chromedriver.exe'

        if os.path.exists(driver_path):
            print(f'chrome driver is installed : {driver_path}')
        else:
            print(f'chrome driver is not installed : {driver_path}')
            print(f'install the chrome driver > version : {chrome_version}')
            chromedriver_autoinstaller.install(True)
            
        selenium_driver_name = 'chrome'    
        selenium_driver_executable_path = driver_path
        selenium_driver_arguments = []
        
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        global driver
        driver = webdriver.Chrome(executable_path=driver_path,
                                  chrome_options=chrome_options)
        return driver
    
    def selenium_movement(driver):
        url = crawl_form.url()
        driver.get(request.url)
        button_element_css = '#_TopArea > div.first_mv_list.current_mv_list._mv_default_list > div > ul > li:nth-child(2) > a > img'
        button = driver.find_element_by_css(button_element_css)
        click = button.click()
        body = to_bytes(text=driver.page_source)
        sleep(3)        
        return HtmlResponse(url=request.url, body=body,encoding='utf-8',request=request)
        
        