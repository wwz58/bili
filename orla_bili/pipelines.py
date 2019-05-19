# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy import log
from twisted.enterprise import adbapi
import time
import sqlite3


class DbSqlitePipeline(object):
    def __init__(self):
        """Initialize"""
        self.__dbpool = adbapi.ConnectionPool('sqlite3',
                                              database='./sqlite.db',
                                              check_same_thread=False)

    def shutdown(self):
        """Shutdown the connection pool"""
        self.__dbpool.close()

    def process_item(self, item, spider):
        """Process each item process_item"""
        query = self.__dbpool.runInteraction(self.__insertdata, item, spider)
        query.addErrback(self.handle_error)
        return item

    def __insertdata(self, tx, item, spider):
        """Insert data into the sqlite3 database"""
        spidername = spider.name
        for img in item['images']:
            tx.execute("select * from data where url = ?", (img['url'],))
            result = tx.fetchone()
            if result:
                log.msg("Already exists in database", level=log.DEBUG)
            else:
                tx.execute( \
                    "insert into data(url, localpath, checksum, created, spidername) values (?,?,?,?,?)", (
                        img['url'],
                        img['path'],
                        img['checksum'],
                        time.time(),
                        spidername)
                )
                log.msg("Item stored in db", level=log.DEBUG)

    def handle_error(self, e):
        log.err(e)


class OrlaImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
