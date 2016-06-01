#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import scrapy
from CSDNblog.items import CsdnblogItem
from scrapy.selector import Selector
from scrapy.http import Request 

class CsdnblogSpider(scrapy.Spider):

	name = "Csdnblog"

	download_delay = 1

	allowed_domains = ["blog.csdn.net"]
	start_urls = (
		"http://blog.csdn.net/u012150179/article/details/11749017",
	)


	def parse(self,response):
#		lis = response.xpath('/html/body/div[4]/div[3]/div[1]/div/div[3]/div[1]/h1/span')

		sel = Selector(response)		

		item = CsdnblogItem()

		article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()  
		article_url = str(response.url)
		item['article_name'] = [n.encode('utf-8') for n in article_name]
		item['article_url'] = article_url.encode('utf-8')

		yield item

#		urls = sel.xpath('//li[@id="next_article"]/a/@href').extract()
		urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()  
		for url in urls:
#			print url
			url = "http://blog.csdn.net" + url
#			print url
			yield Request(url, callback=self.parse)  






























