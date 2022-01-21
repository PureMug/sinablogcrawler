# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class SinablogcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 文章列表项
class BlogIndexItem(scrapy.Item):
    title = Field()
    pubtime = Field()
    url = Field()
    filename = Field()

# 文章内容
class BlogArticleItem(scrapy.Item):
    title = Field()
    pubtime = Field()
    body = Field()
    filename = Field()
