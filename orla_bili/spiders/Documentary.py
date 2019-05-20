import json
import re

from scrapy.spider import Spider
from scrapy.http import Request
from ..items import DocumentaryItem
from scrapy.selector import Selector
from scrapy import log


class DocumentarySpider(Spider):
    name = "Documentary"
    allowed_domains = ["bilibili.com"]
    index_head = 'https://bangumi.bilibili.com/media/web_api/search/result?style_id=-1&producer_id=-1&year=-1&order=2&st=3&sort=0&season_type=3&pagesize=20'
    video_head = 'https://www.bilibili.com/bangumi/media/md'
    start_urls = [index_head + '&page=1']
    summary_p = re.compile('"evaluate":"(.*?)",')
    actor_p = re.compile('"actors":"(.*?)",')
    staff_p = re.compile('"staff":"(.*?)",')

    def parse(self, response):
        js = json.loads(response.body)['result']
        page = js.get('page', None)
        if page is not None:
            log.msg("parse index page %s" % page['num'], level=log.INFO)

            next_idx = int(page['num']) + 1
            next_url = self.index_head + '&page=' + str(next_idx)
            yield Request(next_url, callback=self.parse)
            for vid in js['data']:
                media_id = vid['media_id']
                yield Request(self.video_head + str(media_id), meta=vid, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = DocumentaryItem()
        m = response.meta
        item['image_urls'] = [m.get('cover', '')]
        for name in ['badge', 'badge_type', 'index_show', 'is_finish', 'link', 'media_id', 'season_id',
                     'title']:
            item[name] = m.get(name, None)
        for name in ['play', 'pub_date', 'pub_real_time', 'renewal_time', 'score', 'type']:
            item[name] = m['order'].get(name, None)
        item['media_tags'] = sel.xpath('//*[@class="media-tag"]/text()').extract()
        item['num_long_comment'] = sel.xpath(
            "//div[@class='media-tab-wrp']/div[@class='media-tab-nav']/ul[@class='clearfix']/li[2]/text()").extract()[
                                       0][5:-2]
        item['num_short_comment'] = sel.xpath(
            "//div[@class='media-tab-wrp']/div[@class='media-tab-nav']/ul[@class='clearfix']/li[3]/text()").extract()[
                                        0][5:-2]

        body = response.body

        summary_m = self.summary_p.search(body)
        if summary_m:
            item['summary'] = summary_m.group(1)

        actors_m = self.actor_p.search(body)
        if actors_m:
            item['actors'] = actors_m.group(1)

        staff_m = self.staff_p.search(body)
        if staff_m:
            item['staff'] = staff_m.group(1)
        yield item
