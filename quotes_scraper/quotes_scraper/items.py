import scrapy
class QuoteItem(scrapy.Item):
# define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()