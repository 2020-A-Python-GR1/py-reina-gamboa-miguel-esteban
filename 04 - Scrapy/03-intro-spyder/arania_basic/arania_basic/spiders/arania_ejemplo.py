import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        print(titulos)
        imagenes = etiqueta_contenedora.css(
            'div.image_container a img::attr(src)'   
        ).extract()
        print(imagenes)
        price_product = etiqueta_contenedora.css(
            'div.product_price p.price_color::text'
        ).extract()
        print(price_product)
        stock_procduct = etiqueta_contenedora.css(
            'p.availability::text'
        ).extract()
        print(stock_procduct)
        

# scrapy crawl nombre_arania