#module import
import scrapy
import pandas as pd
import importlib
import os
import sys
# system path append
sys.path.append('../../Pass/')

# Spider Class
class TestModuleSpider(scrapy.Spider):
    name = 'TestModuleSpider'
        
    def start_requests(self):
        
        global get_variables
        def get_variables(input_module):
            return  importlib.import_module(input_module)

        
        global input_module, pass_py
        input_module = self.input_module
        pass_py = get_variables(input_module)
        
        
        url_list = pass_py.crawl_form.urls()
        
        for url in url_list:
            yield scrapy.Request(url,callback=self.parse)
            
    def parse(self, response):
        # pass_py = get_variables(input_module)
        pass_py.crawl_form.parse(response)

##################### 여기까지 완성 ##################################

    def to_middleware():
        # pass_py = get_variables(input_module)
        middle_mod =  pass_py.active_crawl
        return middle_mod
    
#################### Middleware로 넘어감 이제 ^_^ #####################