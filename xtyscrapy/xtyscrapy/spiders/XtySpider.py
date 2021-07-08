import scrapy

from ..items import XtyscrapyItem

class XtySpider(scrapy.Spider):
    name = 'Xtbps'
    start_urls = ['http://www.caict.ac.cn/kxyj/qwfb/bps/']

    FILES_STORE = './'

    def parse(self, response, **kwargs):
        for repo in response.xpath("body/table[last()]//a[contains(@href,'.htm')]"):
            try:
                link_url = repo.css('a::attr(href)').get()
                yield scrapy.Request(self.start_urls[0]+link_url, self.download)
                # yield {
                #     'name': repo.xpath('a/@title').get().replace('\n ', '').strip(),
                #     'link': repo.css('a::attr(href)').get()
                # }
            except: 
                yield scrapy.Request(repo.css('a::attr(href)').get(), self.download)
                # yield {
                #     'name': repo.css('a::attr(title)').get().replace('\n ', '').strip(),
                #     'link': repo.css('a::attr(href)').get()
                # }
        
        # next_page = response.xpath("//div[@class='BtnGroup']/a[contains(@href,'after')]/@href").get()
        # if next_page is not None:
        #     # next_page = next_page.replace('before', 'after')
        #     yield response.follow(next_page, callback=self.parse)
    def download(self, response):
        
        file_url = response.xpath("body/table[last()]//a[contains(@href,'.pdf')]/@href").extract_first()
        url = response.urljoin(response.request.url+"/."+file_url)
        # print("============"+url)

        item = XtyscrapyItem()
        item['file_urls']=[url]
        
    
        return item
