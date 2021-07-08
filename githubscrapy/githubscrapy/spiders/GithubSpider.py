import scrapy

class GithubSpider(scrapy.Spider):
    name = 'Github'
    start_urls = ['https://github.com/lhfei?tab=repositories']

    def parse(self, response, **kwargs):
        for repo in response.css('li.col-12.d-flex.width-full.py-4.border-bottom.color-border-secondary.public.source'):
            try:
                yield {
                    'name': repo.css('a::text').get().replace('\n ', '').strip(),
                    # 'link': repo.css('a::attr(href)').get()
                }
            except: 
                yield {
                    'name': repo.css('a::text').get().replace('\n ', '').strip(),
                    # 'link': repo.css('a::attr(href)').get()
                }
        
        next_page = response.xpath("//div[@class='BtnGroup']/a[contains(@href,'after')]/@href").get()
        if next_page is not None:
            # next_page = next_page.replace('before', 'after')
            yield response.follow(next_page, callback=self.parse)