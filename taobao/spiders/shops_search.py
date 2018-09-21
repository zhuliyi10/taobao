import scrapy

from taobao.items import ShopItem


class ShopsSearch(scrapy.Spider):
    name = 'shops_search'
    search = '家用冰箱'
    page = 0
    start_urls = [
        "https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180921&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}".format(
            search, 0)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    cookies={
        'JSESSIONID':'4A70185EBDC1A032779B57A156072B37',
        'enc':'xasysOEFyIoB3xAqdT2%2B%2BCzXAiz8kGnx4v4N6y%2B9ZGjbIceTSinJwbyE9y1XuOz9BFRfttZm6N30o5YTyvogeg%3D%3D',
        'miid':'957003949809628999',
        '_tb_token_':'e6efefbe6e55d',
        'cookie2':'1aa129f633edde1608e95858a5d80d51',
        'cna':'PNa8E++1u3wCAT2MGpCkN8ho',
        'isg':'BK6u9T34eT3TGI3ZbxzHSTsl_wRwr3KpOfI_CNh3GrFsu04VQD_CuVS5d2fyeGrB'

    }
    def start_requests(self):
        return [scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.headers,cookies=self.cookies)]

    def parse(self, response):

        list = response.xpath("//div[@class='m-itemlist']")
        for item in list:
            shop = ShopItem()
