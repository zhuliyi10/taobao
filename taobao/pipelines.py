# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from taobao.mysql_operate import mysql_operate


class TaobaoPipeline(object):

    def open_spider(self,spider):
        self.sql_operate= mysql_operate()

    def process_item(self, item, spider):
        print(item)
        self.sql_operate.insert_data(item)
        return item
