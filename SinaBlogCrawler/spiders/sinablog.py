import scrapy
from SinaBlogCrawler.items import BlogIndexItem
from SinaBlogCrawler.items import BlogArticleItem

class SinablogSpider(scrapy.Spider):
    name = 'sinablog'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = [
        # 'http://blog.sina.com.cn/s/articlelist_1215172700_1_1.html'，
        'http://blog.sina.com.cn/s/articlelist_1215172700_8_1.html'
    ]

    def parse(self, response):
        url = response.url.split('/')[-1]
        if url.startswith('articlelist_'):
            for item in self.parseIndex(response):
                yield scrapy.Request(item['url'], callback=self.parse)
                yield item

            next_url = self.parseIndexNext(response)
            self.logger.debug('###### next page url=' + ('None' if next_url is None else next_url))
            if next_url is not None:
                yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

        if url.startswith('blog_'):
            item = self.parseArticle(response)
            yield item

    def parseIndex(self, response):
        for each in response.selector.xpath('//div[@class="articleCell SG_j_linedot1"]'):
            item = BlogIndexItem()

            p0a = each.xpath('p[@class="atc_main SG_dot"]//a')
            p1span = each.xpath('p[@class="atc_info"]/span')
            item['title'] = p0a.xpath('text()')[0].extract()
            item['url'] = p0a.xpath('@href')[0].extract()
            item['pubtime'] = p1span.xpath('text()')[0].extract()
            item['filename'] = item['url'].split('/')[-1]
            self.logger.debug(item)
            yield item

    def parseIndexNext(self, response):
        next_url = response.selector.xpath('//div[@class="SG_page"]//a[contains(text(), "下一页")]/@href').extract_first()
        return next_url

    def parseArticle(self, response) -> scrapy.Item:
        item = BlogArticleItem()

        title = response.selector.xpath('//div[@class="articalTitle"]/h2/text()').extract_first()
        pubtime = response.selector.xpath('//div[@class="articalTitle"]/span[@class="time SG_txtc"]/text()').extract_first()
        text = response.selector.xpath('//div[@id="sina_keyword_ad_area2"]').xpath('string()')
        text = text[0].extract().strip()
        article = ''
        for line in text.split('\n'):
            tmp = line.strip()
            if tmp != '' and tmp != '浏览“缠中说禅”更多文章请点击进入缠中说禅':
                article += '<p>' + tmp + '</p>\n'

        item['title'] = title
        item['pubtime'] = pubtime
        item['body'] = article
        item['filename'] = response.url.split('/')[-1]
        self.logger.debug(item)
        return item