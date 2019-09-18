import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.vinabook.com/']

    def parse(self, response):
        for title in response.css('.metro-dropdown-menu h2'):
            yield {'title': title.css(' ::text').get()}
        
        for title in response.css('.nav-sub-list-box a'):
            yield {'title-sub': title.css(' ::text').get(),'url-sub': title.attrib['href']}
        
        #for next_page in response.css('a.next-posts-link'):
            #yield response.follow(next_page, self.parse)