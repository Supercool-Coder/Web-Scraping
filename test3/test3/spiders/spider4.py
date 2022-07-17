import scrapy
from ..items import Test1Item

class Test1(scrapy.Spider):
    name = "uttam"
    start_urls=["https://www.trophyroomstore.com/collections/all/"]

    def parse(self, response, **kwargs):
        items=Test1Item()
        all_uttam = response.css('div.quote')
        for uttam in all_uttam:
            release_location=uttam.css('span.text::text').extract()
            price = uttam.css('.price::text').extract()
            created_at = uttam.css('.created_at::text').extract()
            updated_at = uttam.css('.updated_at::text').extract()
            retailer = uttam.css('.retailer::text').extract()
            available_size = uttam.css('.available_size::text').extract()
            direct_link =  uttam.css('.direct_link::text').extract()
            auto_checkout_link = uttam.css('.auto_checkout_link::text').extract()
            stock_code =  uttam.css('.stock_code::text').extract()

            items['release_location'] = release_location
            items['price'] = price
            items['created_at'] = created_at
            items['updated_at'] = updated_at
            items['retailer'] = retailer
            items['available_size'] = available_size
            items['direct_link'] = direct_link
            items['auto_checkout_link'] = auto_checkout_link
            items[' stock_code'] =  stock_code
            yield items