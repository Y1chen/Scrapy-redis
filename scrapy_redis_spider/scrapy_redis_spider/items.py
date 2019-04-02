# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyRedisSpiderItem(scrapy.Item):
    position = scrapy.Field()    # 职位名称
    company = scrapy.Field()    # 公司名称
    address = scrapy.Field()    # 工作地点
    money = scrapy.Field()    # 薪水
    content = scrapy.Field()    # 具体要求
