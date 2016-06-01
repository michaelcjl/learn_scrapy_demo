#!/usr/bin/python  
# -*- coding:utf-8 -*-  
  
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as SE
from doubanmovies.items import DoubanmoviesItem 



class DoubanmovieSpider(CrawlSpider):  
	"""爬虫DoubanmoviesItem"""  
	
	name = "Doubanmovies"  
	
	#减慢爬取速度 为1s  
	#download_delay = 3  
	allowed_domains = ["movie.douban.com"]  
	start_urls = [   
		#第一篇文章地址  
		"https://movie.douban.com/top250?start=0&filter="
	]  

	rules = [
        Rule(SE(allow=("\?start=\d{1,}&filter=")), 
                         follow=True,
                         callback='parse_item')
    ]

	
	def parse_item(self, response):
        #print "-----------------"
		items = []
		sel = Selector(response)	
		lis = sel.xpath('//ol[@class="grid_view"]/li')   
 
		for li in lis:
			item = DoubanmoviesItem()   			

			item['rank'] = li.xpath('div/div[1]/em/text()')[0].extract() 
			item['name'] = li.xpath('div/div[2]/div[1]/a/span[1]/text()')[0].extract()

			items.append(item)
			
		return items







