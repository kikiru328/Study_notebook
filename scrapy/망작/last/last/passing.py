import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import warnings
warnings.filterwarnings("ignore")
import time
import datetime


global url
def url():
    selenium_open_url = 'https://velog.io/@poiuyy0420/Scrapy-settings.py%EC%99%80-%ED%8C%8C%EC%9D%BC%EB%82%B4%EB%B3%B4%EB%82%B4%EA%B8%B0#settings'
    return selenium_open_url

global Chrome_selenium_setting
def Chrome_selenium_setting():
    # re_text
    import chromedriver_autoinstaller
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import os

    chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'{chrome_version}\chromedriver.exe'

    if os.path.exists(driver_path):
        print(f'chrome driver is installed : {driver_path}')
    else:
        print(f'chrome driver is installed : {driver_path}')
        print(f'install the chrome driver > version : {chrome_version}')
        print(f'install complete > {driver_path}')
        chromedriver_autoinstaller.install(True)
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(executable_path = driver_path,
                                chrome_options=chrome_options)
    return driver

def selenium_movement(driver):
    from scrapy.http import HtmlResponse
    from scrapy.utils.python import to_bytes
    import time
    
    bike_company = driver.find_element_by_css_selector("#root > div.sc-iAKWXU.sc-efQSVx.fVREVI > div.sc-kfPuZi.gtFVlQ > div > div.sc-bkkeKt.kMpGa > a.user-logo")
    bike_company.click()
    
    body = to_bytes(text=driver.page_source)
    time.sleep(5)
    return  body
    
    # import scrapy
    # # selenium 실행
    # # driver = Chrome_selenium_setting()
        
    # # # selenium 움직임 설정
    # import datetime
    
    # def doScrollDown(whileSeconds):
    #     start = datetime.datetime.now()
    #     end = start + datetime.timedelta(seconds=whileSeconds)
    #     while True:
    #         driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #         time.sleep(1)
    #         if datetime.datetime.now() > end:
    #             break
            
    # doScrollDown(3)
    
    # get_link_xpath = '//*[@data-qa-locator="product-item"]//a[text()]'
    # for link_el in get_link_xpath:
    #     href = link_el.get_attribute('href')
    #     yield scrapy.Request(href)
    
    driver.quit()
    
    # click_x_path = '//*[@id="main_pack"]/section[1]/div[2]/a/span'
    # driver.get(url())
    # body = driver.find_element_by_xpath(click_x_path)
    # body.click()
    # time.sleep(1)
    
    # text_list_xpath = '//*[@id="lifeIndex"]/div[2]/ul'
    # text_list_elements = driver.find_elements.by_xpath(text_list_xpath)
    # for text in text_list_elements:
    #     href = text.get_attribute('href')
    #     yield scrapy.Request(href)

    # # selenium 종료
    # driver.quit()

global parse   
def parse(response):
    # price = response.css('#container > main > div > div.area-view > div.article-view > div > p:nth-child(20) > b ::text').get()
    response.text
    # yield price
    



