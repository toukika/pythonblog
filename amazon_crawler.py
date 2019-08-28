# -*- coding: utf-8 -*-
import scrapy


class AmazonCrawlerSpider(scrapy.Spider):
    name = 'amazon_crawler'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    def parse(self, response):
        pass
