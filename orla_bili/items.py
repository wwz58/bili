# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AnimeItem(Item):
    # define the fields for your item here like:
    # name = Field()
    badge = Field()
    badge_type = Field()
    index_show = Field()
    is_finish = Field()
    link = Field()
    media_id = Field()
    season_id = Field()
    title = Field()
    follow = Field()
    play = Field()
    pub_date = Field()
    pub_real_time = Field()
    renewal_time = Field()
    score = Field()
    type = Field()

    image_urls = Field()
    images = Field()

    media_tags = Field()
    num_long_comment = Field()
    num_short_comment = Field()
    summary = Field()
    actors = Field()
    staff = Field()


class GuoChuangItem(Item):

    badge = Field()
    badge_type = Field()
    index_show = Field()
    is_finish = Field()
    link = Field()
    media_id = Field()
    season_id = Field()
    title = Field()
    follow = Field()
    play = Field()
    pub_date = Field()
    pub_real_time = Field()
    renewal_time = Field()
    score = Field()
    type = Field()

    image_urls = Field()
    images = Field()

    media_tags = Field()
    num_long_comment = Field()
    num_short_comment = Field()
    summary = Field()
    actors = Field()
    staff = Field()


class MovieItem(Item):
    badge = Field()
    badge_type = Field()
    index_show = Field()
    is_finish = Field()
    link = Field()
    media_id = Field()
    season_id = Field()
    title = Field()
    play = Field()
    pub_date = Field()
    pub_real_time = Field()
    renewal_time = Field()
    score = Field()
    type = Field()

    image_urls = Field()
    images = Field()

    media_tags = Field()
    num_long_comment = Field()
    num_short_comment = Field()
    summary = Field()
    actors = Field()
    staff = Field()


class DocumentaryItem(Item):
    badge = Field()
    badge_type = Field()
    index_show = Field()
    is_finish = Field()
    link = Field()
    media_id = Field()
    season_id = Field()
    title = Field()
    play = Field()
    pub_date = Field()
    pub_real_time = Field()
    renewal_time = Field()
    score = Field()
    type = Field()

    image_urls = Field()
    images = Field()

    media_tags = Field()
    num_long_comment = Field()
    num_short_comment = Field()
    summary = Field()
    actors = Field()
    staff = Field()


class TVItem(Item):
    badge = Field()
    badge_type = Field()
    index_show = Field()
    is_finish = Field()
    link = Field()
    media_id = Field()
    season_id = Field()
    title = Field()
    play = Field()
    pub_date = Field()
    pub_real_time = Field()
    renewal_time = Field()
    score = Field()
    time_show = Field()
    type = Field()

    image_urls = Field()
    images = Field()

    media_tags = Field()
    num_long_comment = Field()
    num_short_comment = Field()
    summary = Field()
    actors = Field()
    staff = Field()
