# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter

from SinaBlogCrawler.items import BlogArticleItem, BlogIndexItem
from .ebook_patterns import CalibrePattern

class SinablogcrawlerPipeline:
    indexes = []
    output_dir = 'output'

    def process_item(self, item, spider):
        if isinstance(item, BlogIndexItem):
            return self.process_index(item, spider)
        if isinstance(item, BlogArticleItem):
            return self.process_article(item, spider)

        spider.logger.debug('process list......' + item)
        return item

    def close_spider(self, spider):
        spider.logger.debug('===>>> when spider closed')
        with open(self.output_dir + os.sep + 'toc', 'w') as f:
            for index, val in enumerate(reversed(self.indexes), 1):
                oldname = val['filename']
                newname = ('0000' + str(index))[-4:] + '.html'
                tmp = CalibrePattern.navmap_pattern.replace('$n', str(index)).replace('$title', val['title']).replace('$filename', newname)
                f.write(tmp)
                os.rename(self.output_dir + os.sep + oldname, self.output_dir + os.sep + newname)

    def process_article(self, item, spider):
        spider.logger.debug('process article item:' + item['title'])
        html = CalibrePattern.html_pattern.replace('$title', item['title']).replace('$pubtime', item['pubtime']).replace('$body', item['body'])

        filename = self.output_dir + os.sep + item['filename']
        spider.logger.debug('saving article:' + filename)
        with open(filename, 'w') as f:
            f.write(html)
        return item

    def process_index(self, item, spider):
        spider.logger.debug('processing index:' + item['title'])
        self.indexes.append(item)
        return item
