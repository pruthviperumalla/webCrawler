import scrapy


class QuotesSpider(scrapy.Spider):
    name = "groupon"

    def start_requests(self):
        urls = []
        for i in range(20):
            new_url = "https://www.groupon.com/goods/electronics?page=%d"%(i+1)
            print new_url
            urls.append(new_url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url in response.selector.css("figure a").xpath("@href").extract():
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
    	yield {'title': response.css("h1.deal-page-title::text").extract_first() ,
    			'price': response.css("div.breakout-option-price::text").extract_first(),
    			'description' : response.css("article div section ul li::text").extract(), 
    			'reviews' : response.css("div.review-text::text").extract(), 
    			}

       
    