import datetime
import time

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ExampleSpider(scrapy.Spider):
    name = "spider"
    # allowed_domains = ["books.toscrape.com/"]

    start_urls = ['https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?is_high_rating=t'] + [
        f"https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?is_high_rating=t&page={i}" for i in range(2, 11)
    ]

    def parse(self, response):
        cards = response.xpath('//div[@id="paginatorContent"]/div/div')
        for card in cards:
            print(len(cards), "Количество")
            try:
                price = ''.join([i for i in card.css('span.c3128-a1::text').get() if i.isdigit()])
            except Exception as ex:
                print(ex)
            yield {
                'name': card.xpath('.//span[@class="tsBody400Small"]/text()').get(),
                'link': card.xpath('.//a/@href').get(),
                'price': price
            }