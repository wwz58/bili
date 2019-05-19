from scrapy.spider import Spider
from ..items import GuoChuangItem


class GuochuangSpider(Spider):
    name = "GuoChuang"
    allowed_domains = ["bilibili.com"]
    start_urls = (
        'http://www.bilibili.com/',
    )

    def parse(self, response):
        yield GuoChuangItem(test='guochuang')
