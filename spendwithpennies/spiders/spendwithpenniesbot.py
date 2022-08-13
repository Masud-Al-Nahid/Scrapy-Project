import scrapy
from ..items import SpendwithpenniesItem

with open('swp.txt'): as file:
    urllist = file.readlines()

urllist = [x.strip() for x in urllist]


class SpendwithpenniesbotSpider(scrapy.Spider):
    name = 'spendwithpenniesbot'
    start_urls = urllist
    # start_urls = ['https://www.spendwithpennies.com/roasted-asparagus-tarragon-vinaigrette']

    def parse(self, response):
        items = SpendwithpenniesItem()
        title = response.css('title::text').get()
        url = response.url
        items ['h1'] = response.css('h1::text').get()
        items['title'] = title
        items['url'] = url
        yield items