import scrapy

# Class
class MovieSpider(scrapy.Spider):
    # Spider name
    name = 'Movie'
    
    def start_requests(self):
        urls = ['https://movie.naver.com/movie/running/current.nhn']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # response.css() vs response.xpath()
        movie_list = response.css('ul.lst_detail_t1 > li')
        for movie in movie_list:
            title = movie.css('.tit > a::text').get()
            print('title', title)
        
        
    