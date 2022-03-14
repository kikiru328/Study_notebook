class crawl_form:
    def urls():
        urls = ['https://movie.naver.com/movie/bi/mi/basic.naver?code=190991',
        'https://movie.naver.com/movie/bi/mi/basic.naver?code=154282']
        return urls

    def parse(response):
        visitors = response.css('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(10) > div > p.count::text').get()
        print(f'관객수 > {visitors}')
        # l = ItemLoader(item = MovieItem(), selector=response)
        # l.add_css('관객수','p.count::text')
        # yield l.load_item()

class active_crawl:
    
    # global chrome_driver_selenium
    def chrome_driver_selenium():
        import chromedriver_autoinstaller
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from time import time
        import os

        chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        driver_path = f'{chrome_version}\chromedriver.exe'

        if os.path.exists(driver_path):
            print(f'chrome driver is installed : {driver_path}')
        else:
            print(f'chrome driver is not installed : {driver_path}')
            print(f'install the chrome driver > version : {chrome_version}')
            chromedriver_autoinstaller.install(True)
            
            
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        
        driver = webdriver.Chrome(executable_path=driver_path,
                                  chrome_options=chrome_options)
        return driver
    
    # def selenium_opt():
    #     from scrapy.http import HtmlResponse
    #     from scrapy.utils.python import to_bytes
    #     driver = chrome_driver_selenium()
    #     from selenium.webdriver.chrome.options import options
    #     from time import sleep
        
        