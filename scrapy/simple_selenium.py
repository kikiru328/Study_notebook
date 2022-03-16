import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy.crawler import CrawlerProcess
class drinkSpider(scrapy.Spider):
    name = "drink"
    def start_requests(self):
        yield SeleniumRequest(
        url='https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg=1',
        callback=self.parse,
        wait_time=3,
        wait_until=EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/section[4]/div[2]/nav/button[2]'))
            )
    def parse(self, response):
        product = response.css('li.product-grid__item')
        for item in product:
            yield{
                'name' :item.css('p.product-card__meta::text').get()
            }
            
process = CrawlerProcess(
    settings = {
        'FEEDS' : {
            'whisky.csv':{'format': 'csv'}
    }}
)

process.crawl(drinkSpider)
process.start()
