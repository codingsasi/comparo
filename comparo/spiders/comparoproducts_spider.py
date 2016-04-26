import scrapy
from comparo.items import ProductLineItem, ProductItem
import re
import time

class FlipkartProductsSpider(scrapy.Spider):
    name = 'flipkartproducts'
    allowed_domains = ['www.flipkart.com', 'flipkart.com']
    start_urls = [
        'http://www.flipkart.com/televisions?otracker=hp_mod_electronics_vis_Television',
        'http://www.flipkart.com/laptops/pr?sid=6bo,b5g'
    ]

    def parse(self, response):
        merchandise = ProductItem()
        merchandise['time'] = time.time()
        merchandise['category'] = response.css('h1::text').extract_first()

        products = []
        for price_tile in response.css('.product-unit'):
            productline = ProductLineItem()
            productline['name'] = price_tile.css('.pu-details .pu-title > a::attr(title)').extract_first()
            productline['stars'] = price_tile.css('.pu-details .pu-rating div.fk-stars-small::attr(title)').extract_first()
            productline['ratings'] = price_tile.css('.pu-details .pu-rating::text').extract_first()
            productline['price'] = price_tile.css('.pu-details .pu-price .pu-final span::text').extract_first()
            products.append(productline)

        merchandise['products'] = products
        return merchandise

class AmazonProductsSpider(scrapy.Spider):
    name = 'amazonproducts'
    allowed_domains = ['www.amazon.in', 'amazon.in']
    start_urls = [
        'https://www.amazon.in/TVs/b/ref=sv_e_6?ie=UTF8&node=1389396031',
        'https://www.amazon.in/Laptops/b/ref=sv_pc_2?ie=UTF8&node=1375424031'
    ]

    def parse(self, response):
        merchandise = ProductItem()
        merchandise['time'] = time.time()
        merchandise['category'] = response.css('h1::text').extract_first()

        products = []
        for price_tile in response.css('li.s-result-item'):
            productline = ProductLineItem()
            productline['name'] = price_tile.css('.a-spacing-mini h2::text').extract_first()
            productline['stars'] = price_tile.css('.a-spacing-none i.a-icon-star > span::text').extract_first()
            #temp = price_tile.css('.a-spacing-none').extract()[8]
            #productline['ratings'] = temp.css('a.a-size-small.a-link-normal.a-text-normal::text').extract_first()
            #productline['ratings'] = price_tile.xpath('//div[@class="a-spacing-none"]//a[@class="a-size-small a-link-normal a-text-normal"]/last()/text()')
            productline['ratings'] = ""
            productline['price'] = price_tile.css('.a-spacing-none span.a-size-base.a-color-price.s-price.a-text-bold::text').extract_first()
            products.append(productline)

        merchandise['products'] = products
        return merchandise
