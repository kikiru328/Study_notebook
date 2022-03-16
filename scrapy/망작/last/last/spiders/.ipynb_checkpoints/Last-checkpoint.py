import scrapy
# from scrapy.utils.project import get_project_settings
import sys
# sys.path.append('../../pass/')
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import importlib

class LastSpider(scrapy.Spider):
    name = 'Last'
    
    def get_module(self):
        global pass_py
        pass_py = importlib.import_module(self.import_module)
        return pass_py 
    
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
        'last.middlewares.LastDownloaderMiddleware' : 100
        }
    }
    
    # def start_requests(self):
        
    #     global pass_py
    #     pass_py = importlib.import_module(self.module_name)
  
        
    #     # settings = get_project_settings()
    #     # driver = settings.selenium_driver_set()
    #     # driver = pass_py.Chrome_selenium_setting()
    #     # pass_py.selenium_movement(driver)
    #     # text = pass_py.selenium_movement()
    #     # print(url)
    #     # def get_module_name():
    #     #     return pass_py.name
        
        
    def parse(self, response):
        # pass
        print(pass_py.parse(response))
