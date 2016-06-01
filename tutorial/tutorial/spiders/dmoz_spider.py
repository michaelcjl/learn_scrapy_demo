# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = (
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"

    )

    def parse(self, response):
#        filename = response.url.split('/')[-2] + ".html"
#		with open(filename,'wb') as fp:
#			fp.write(response.body)
		lis = response.xpath('/html/body/div[2]/div[3]/fieldset[3]/ul/li')
		for li in lis:
			item = TutorialItem()
		    item['title'] = li.xpath(('a/text()').extract()
            item['desc'] = li.xpath('text()').extract()
			item['link'] = li.xpath('a/@href').extract()
			yield item












