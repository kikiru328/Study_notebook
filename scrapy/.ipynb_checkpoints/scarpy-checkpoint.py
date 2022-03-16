# import scrapy

# Class
# class MovieSpider(scrapy.Spider):
#     # Spider name
#     name = 'movie'
#     def __init__(self,urls=None, title_css=None):
#         self.urls= self.urls
#         self.title_css = self.title_css
    
#     def start_requests(self):
#         # urls = ['https://movie.naver.com/movie/running/current.nhn'] 
#         # for url in self.urls:
#         for url in self.urls:
#             print(url)
#             yield scrapy.Request(url=url, callback=self.parse)
    
#     def parse(self, response):
#         # response.css() vs response.xpath()
#         movie_list = response.css('ul.lst_detail_t1 > li')
        
#         for movie in movie_list:
#             # title = movie.css('.tit > a::text').get()
#             title = movie.css(self.title_css).get()
#             rate = movie.css('.num::text').get()
#             # rate = movie.css(self.title_css).get()
#             director = movie.css('.info_txt1 > dd > span.link_txt > a::text').get()
#             print('title', title)
#             print('rate', rate)
#             print('director', director)
#             print('director', director)