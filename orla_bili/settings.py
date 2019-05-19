# Scrapy settings for orla_bili project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'orla_bili'

SPIDER_MODULES = ['orla_bili.spiders']
NEWSPIDER_MODULE = 'orla_bili.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'orla_bili (+http://www.yourdomain.com)'

from datetime import date
today = date.today().strftime('%Y%m%d')
FEED_URI = 'feeds/%(name)s/' + today +'.csv'
FEED_FORMAT = 'csv'

IMAGES_STORE = './feeds'
# IMAGES_EXPIRES = 90

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
