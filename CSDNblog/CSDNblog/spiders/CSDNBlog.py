# -*- coding:utf-8 -*-  
  
import scrapy
from scrapy.spiders import CrawlSpider, Rule  
from scrapy.linkextractors.sgml import SgmlLinkExtractor  
from scrapy.selector import Selector  
from CSDNblog.items import CsdnblogItem

  
  
class CSDNBlogCrawlSpider(CrawlSpider):  
  
    """继承自CrawlSpider，实现自动爬取的爬虫。"""  
  
    name = "CSDNBlogCrawlSpider"  
    #设置下载延时  
    download_delay = 0.1  
    allowed_domains = ['blog.csdn.net']  
    #第一篇文章地址  
    start_urls = ['http://blog.csdn.net/u012150179/article/details/11749017']  
  
    #rules编写法一，官方文档方式  
    #rules = [  
    #    #提取“下一篇”的链接并**跟进**,若不使用restrict_xpaths参数限制，会将页面中所有  
    #    #符合allow链接全部抓取  
    #    Rule(SgmlLinkExtractor(allow=('/u012150179/article/details'),  
    #                          restrict_xpaths=('//li[@class="next_article"]')),  
    #         follow=True)  
    #  
    #    #提取“下一篇”链接并执行**处理**  
    #    #Rule(SgmlLinkExtractor(allow=('/u012150179/article/details')),  
    #    #     callback='parse_item',  
    #    #     follow=False),  
    #]  
  
    #rules编写法二，更推荐的方式（自己测验，使用法一时经常出现爬到中间就finish情况，并且无错误码）  
    rules = [  
        Rule(scrapy.linkextractors.LinkExtractor(allow=('/u012150179/article/details'),  
                              restrict_xpaths=('//li[@class="next_article"]')),  
             callback='parse_item',  
             follow=True)  
    ]  
  
    def parse_item(self, response):  
  
        #print "parse_item>>>>>>"  
        item = CsdnblogItem()  
        sel = Selector(response)  
        blog_url = str(response.url)  
        blog_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()  
  
        item['article_name'] = [n.encode('utf-8') for n in blog_name]  
        item['article_url'] = blog_url.encode('utf-8')  
  
        yield item  
































'''
#!/usr/bin/python  
# -*- coding:utf-8 -*-  

import scrapy
from CSDNblog.items import CsdnblogItem
from scrapy.selector import Selector

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

		urls = sel.xpath('//li[@id="next_article"]/a/@href').extract()
		for url in urls:
			print url
			url = "http://blog.csdn.net" + url
			print url
			yield Request(url, callback=self.parse)  



'''



























