# Description: First tutorial on scrapy web crawling tool.
# Date: 2022-06-17
# Source: https://docs.scrapy.org/en/latest/intro/tutorial.html

# initialize tutorial project
scrapy startproject tutorial

# crawl site
cd tutorial
scrapy crawl quotes

# shell to scrape
scrapy shell "https://quotes.toscrape.com/page/1/"
#>>> response.css('title')
#>>> response.css('title').getall()
#>>> response.css('title::text').getall()
#>>> response.css('title::text').get()
#>>> response.css("noelement").get()
#>>> response.css('title::text').re(r'Quotes.*')
#>>> response.css('title::text').re(r'blah.*')
#>>> response.css('title::text').re(r'(\w+) to (\w+)')