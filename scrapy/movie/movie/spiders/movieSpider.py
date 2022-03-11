import scrapy
import pandas as pd
# Class
import sys
sys.path.append('../PASS/')
import importlib

from movie.items import MovieItem
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class MovieSpider(scrapy.Spider):
    # Spider name
    name = 'test'
        
    def start_requests(self):
        mod = importlib.import_module(self.module_name)
        url_list = mod.urls()
        for url in url_list:
            yield scrapy.Request(url,callback=self.parse)

    
    def parse(self, response):
        # response.css() vs response.xpath()
        l = ItemLoader(item = MovieItem(), selector=response)
        l.add_css('관객수','p.count::text')
        yield l.load_item()
        # item['관객수'] = response.css('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(10) > div > p.count::text').get()
        
            
    
        # movie_list = response.css('ul.lst_detail_t1 > li')
        # for movie in movie_list:
        #     title = movie.css('.tit > a::text').get()
        #     # title = movie.css(self.css_).get()
        #     rate = movie.css('.num::text').get()
        #     director = movie.css('.info_txt1 > dd > span.link_txt > a::text').get()
        #     print('title', title)
        #     print('rate', rate)
        #     print('director', director)
        process = CrawlerProcess(settings = {
            # excport
            'Feed_uri' : 'movie.csv',
            'Feed_format' : 'csv'
        })
        process.crawl(MovieSpider)
 
    # content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(4) > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a