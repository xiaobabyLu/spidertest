import scrapy


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains =['dmoz.org']

    start_urls = [
        "http://dmoztools.net/Computers/E-Books/",
        "http://dmoztools.net/Health/"
    ]

    def parse(self, response):
        filename =response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)