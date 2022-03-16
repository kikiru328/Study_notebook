import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import warnings
warnings.filterwarnings("ignore")
import time

# import python file
import chrome_driver_auto
driver_path = chrome_driver_auto.Chrome_driver.install_driver_path()
chrome_option = chrome_driver_auto.Chrome_driver.chrome_option()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
# driver = webdriver.Chrome(executable_path = driver_path, chrome_options=chrome_option)


# setting url for selenium
class crawling:
    def __init__(self,driver_path, chrome_option,elements):
        self.driver_path = driver_path
        self.chrome_option = chrome_option
        self.elements = elements
        
    def url():
        from urllib import parse
        keyword = [parse.quote('금연정책')]
        start_url = f'https://www.youtube.com/results?search_query={keyword}&sp=CAISAhAB'
        return start_url

    def selenium_movement(self,driver_path,chrome_option):
        driver = webdriver.Chrome(executable_path = driver_path,chrome_options=chrome_option)
        
        # movement
        body = driver.find_element_by_xpath('/html/body')
        time.sleep(2)
        while True:
            if driver.find_element_by_id('message').text.strip() == '결과가 더 이상 없습니다.':
                print('nope')
                break
            body.send_keys(Keys.PAGE_DOWN)
        # search_box.send_keys('빅데이터')
        # search_box.send_keys(Keys.RETURN)
        soup = bs(driver.page_source, 'html.parser')
        # time.sleep(2)
        # searching = driver.find_element_by_xpath('//*[@id="Odp5De"]/div/div/div/div[2]/div[1]/div[2]/g-more-link/a/div/span[2]').click()
        # time.sleep(1)
        # # element list
        # elements = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div/div/a/h3')
        return soup

    def parse(response):
        title = response.css('//*[@id="rso"]/div/div/div/div/a/h3::text').get()
        print(title)
            