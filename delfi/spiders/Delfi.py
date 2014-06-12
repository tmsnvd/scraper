from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from delfi.items import DelfiItem

class DelfiSpider(CrawlSpider):
    name = 'Delfi'
    allowed_domains = ['delfi.lt']
    #start_urls = ['http://www.delfi.lt/archive/index.php?tod=12.06.2014&fromd=01.05.2014&channel=908&category=20172&query=']
    #start_urls = ['http://www.delfi.lt/archive/index.php?fromd=01.05.2014&tod=12.06.2014&channel=908&category=20172&query=&page=2']
    #start_urls = ['http://www.delfi.lt/archive/index.php?tod=01.05.2014&fromd=01.03.2014&channel=908&category=20172&query=']
    start_urls = ['http://www.delfi.lt/archive/index.php?fromd=01.03.2014&tod=01.05.2014&channel=908&category=20172&query=&page=2']


    rules = (
        Rule(SgmlLinkExtractor(allow=r'mokslas/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        sel = Selector(response)
        i = DelfiItem()
        i['title'] = sel.xpath('//title/text()').extract()
        i['link'] = response.url
        i['description'] = sel.xpath('//div[@class="delfi-article-body"]').extract()
        return i
