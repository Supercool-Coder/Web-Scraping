# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    release_location = scrapy.Field()
    price = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    retailer = scrapy.Field()
    available_size = scrapy.Field()
    direct_link = scrapy.Field()
    auto_checkout_link = scrapy.Field()
    stock_code = scrapy.Field()
    pass


class Test1Item:
    release_location = scrapy.Field()
    price = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    retailer = scrapy.Field()
    available_size = scrapy.Field()
    direct_link = scrapy.Field()
    auto_checkout_link = scrapy.Field()
    stock_code = scrapy.Field()
    pass