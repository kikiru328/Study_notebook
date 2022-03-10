import scrapy
import sys
sys.path.append('../PASS')
# Class

class MovieSpider(scrapy.Spider):
    # Spider name
    name = 'test'
    
    # # Call passing Variable
    # def variable(self):
    #     global passings
    #     module_name = self.pyfile
    #     import module_name as passings
   
    def start_requests(self):
        # urls = ['https://movie.naver.com/movie/running/current.nhn']
        with open('Passing.txt','r') as passing:
            
        yield scrapy.Request(url=passings.url, callback=self.parse)
    
    def parse(self, response):
        # response.css() vs response.xpath()
        movie_list = response.css('ul.lst_detail_t1 > li')
        for movie in movie_list:
            title = movie.css('.tit > a::text').get()
            title = movie.css('.tit > a::text').get()
            rate = movie.css('.num::text').get()
            director = movie.css('.info_txt1 > dd > span.link_txt > a::text').get()
            print('title', title)
            print('rate', rate)
            print('director', director)
        
        
    #content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(4) > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a