import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import BatakItem


class BatakSpider(scrapy.Spider):
	name = 'batak'
	start_urls = ['http://batak.bg/']

	def parse(self, response):
		posts = response.xpath('//div[@class="tabcontent" and @id="country1"]').getall()
		posts = posts[0].split('<br>')

		for post in posts:
			post = remove_tags(post)
			if len(post) > 41:
				item = ItemLoader(item=BatakItem(), response=response)
				item.add_value('post', post.replace('\n', ' ').replace("'", '"').strip())
				yield item.load_item()






