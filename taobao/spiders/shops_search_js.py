import json

import scrapy

from taobao.items import ShopItem


class ShopsSearch(scrapy.Spider):
    name = 'shops_search_js'
    search = '家用冰箱'
    page = 0
    url_format = "https://s.taobao.com/search?ajax=true&q={}&s={}"
    start_urls = [
        url_format.format(search, page * 44)
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    cookies = {
        'JSESSIONID': '4A70185EBDC1A032779B57A156072B37',
        'enc': 'xasysOEFyIoB3xAqdT2%2B%2BCzXAiz8kGnx4v4N6y%2B9ZGjbIceTSinJwbyE9y1XuOz9BFRfttZm6N30o5YTyvogeg%3D%3D',
        'miid': '957003949809628999',
        '_tb_token_': 'e6efefbe6e55d',
        'cookie2': '1aa129f633edde1608e95858a5d80d51',
        'cna': 'PNa8E++1u3wCAT2MGpCkN8ho',
        'isg': 'BK6u9T34eT3TGI3ZbxzHSTsl_wRwr3KpOfI_CNh3GrFsu04VQD_CuVS5d2fyeGrB'

    }

    def start_requests(self):
        return [scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.headers, cookies=self.cookies)]

    def parse(self, response):
        result = response.text.lstrip().rstrip()
        print("请求的结果：", result)

        json_load = json.loads(result)
        list = json_load['mods']['itemlist']['data']['auctions']

        for item in list:
            shop = ShopItem()
            shop['item_id'] = item['nid']
            shop['title'] = item['title']
            shop['price'] = item['view_price']
            shop['address'] = item['item_loc']
            shop['sold'] = item['view_sales'][0:-3]
            shop['store_name'] = item['nick']
            yield shop

        if (len(list) > 0 and self.page < 30):
            self.page = self.page + 1
            next_url = self.url_format.format(self.search, self.page * 44)
            print('-----', next_url, '-----')
            yield scrapy.Request(next_url, callback=self.parse, headers=self.headers, cookies=self.cookies)
