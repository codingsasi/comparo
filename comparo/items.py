# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComparoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductLineItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    ratings = scrapy.Field()

class ProductItem(scrapy.Item):
    category = scrapy.Field()
    time = scrapy.Field()
    products = scrapy.Field()
