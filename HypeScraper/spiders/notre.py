import scrapy

class NotreSpider(scrapy.Spider):
    name = 'notre'
    
    start_urls = ['https://www.notre-shop.com/collections/sale']
    
    pageNumber = 0

    def parse(self, response):
        self.pageNumber += 1
        print("page {}".format(self.pageNumber))
        product_pages = response.css('.collection__products a')
        yield from response.follow_all(product_pages, self.parse_products)

        pagination_links = response.css('.pagination ul a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_products(self, response):
        SKU = response.css('.product__copy-sub+ p::text').get()
        yield {
            'SKU' : SKU[5:]
        }