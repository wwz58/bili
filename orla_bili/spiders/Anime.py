from scrapy.spider import Spider
from ..items import AnimeItem


class AnimeSpider(Spider):
    name = "Anime"
    allowed_domains = ["bilibili.com"]
    start_urls = (
        'http://www.bilibili.com/',
    )

    def parse(self, response):
        item = AnimeItem()
        item['md_id'] = '2'
        item['image_urls'] = [
            'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1986179278,1118313821&fm=27&gp=0.jpg']
        yield item
