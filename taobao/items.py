# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ShopItem(scrapy.Item):
    # define the fields for your item here like:
    item_id = Field()
    price = Field()
    sold = Field()
    title = Field()
    store_name = Field()
    address = Field()
    pass
