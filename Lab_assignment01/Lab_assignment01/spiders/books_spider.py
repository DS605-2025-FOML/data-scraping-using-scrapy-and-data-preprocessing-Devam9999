import scrapy 
from ..items import book_scrap
class QuotesSpider(scrapy.Spider): 
    name = "book"  # Unique name for the spider 
    start_urls = [ 
        'https://books.toscrape.com/', 
    ] 
 
    def parse(self, response): 
        # This method is called to handle the response downloaded for each request made. 
         
        # We use CSS selectors to find the HTML elements containing the data. 
        all_div_book = response.css('article.product_pod') 
         
        # Create an instance of our item  
 
        for book_div in all_div_book:
            items = book_scrap()
            # Extract data using CSS selectors 
            book_name = book_div.css('h3 a::attr(title)').extract_first() 
            price = book_div.css('.price_color::text').extract_first() 
            rating = book_div.css('p.star-rating::attr(class)').extract() 
            stock = book_div.css('.availability::text').extract()
            stock = " ".join(stock).strip()
            
            # Populate the item fields 
            items['book_name'] = book_name 
            items['price'] = price
            items['rating'] = rating  
            items['stock'] = stock 
 
            # Yield the populated item to the Scrapy engine 
            yield items 
 
        # Find the 'Next' button link and follow it if it exists 
        next_page = response.css('li.next a::attr(href)').get() 
 
        if next_page is not None: 
            # The 'response.follow' method handles relative URLs automatically 
            yield response.follow(next_page, callback=self.parse) 