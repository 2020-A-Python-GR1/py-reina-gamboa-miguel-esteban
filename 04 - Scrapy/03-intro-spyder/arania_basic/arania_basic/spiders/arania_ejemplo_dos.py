import scrapy

class IntroSpider(scrapy.Spider):
    name = 'intro_spider_fybeca'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]
    