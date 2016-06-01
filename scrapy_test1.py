#!/usr/bin/env python
# encoding: utf-8

import scrapy

class StackOverflowSpider(scrapy.Spider):
	name = "finance_china"
	start_urls=["http://www.zaobao.com.sg/finance/china"]

	def parse(self, response):
		for href in response.css('.l_header h1 a::attr(href)'):
			full_url = response.urljoin(href.extract())			
			yield scrapy.Request(full_url,callback=self.parse_question)


	def parse_question(self, response):
		yield {
			'title':response.css('h1::text').extract()[0],
			
#			'body':response.css(".a_body").extract()[0],
			
			'link':response.url,
			}


