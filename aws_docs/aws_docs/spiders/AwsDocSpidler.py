import scrapy

class AwsDocSpidler(scrapy.Spider):
    name = 'AWS'
    language = 'en_us'
    start_urls = ['https://docs.aws.amazon.com/'+str(language)+"/"]

    FILES_STORE = './'

    def parse(self, response, **kwargs):
        for repo in response.xpath("//body//ol[contains(@class,'awsui-cards-container')]//li[contains(@class, 'awsui-cards-card-container')]//span[contains(@class, 'awsui-cards-card-header-inner')]/span/h4"):
            try:
                print("++++++++++++++++++++++++")
                link_url = repo.css('a::attr(href)').get()
                print(">>>>>>>>>>>>>>>>>>>>"+repo)
                # yield {
                #     'name': repo.xpath('a/@title').get().replace('\n ', '').strip(),
                #     'link': repo.css('a::attr(href)').get()
                # }
            except: 
                print('===========================error')
                # yield {
                #     'name': repo.css('a::attr(title)').get().replace('\n ', '').strip(),
                #     'link': repo.css('a::attr(href)').get()
                # }
        
        # next_page = response.xpath("//div[@class='BtnGroup']/a[contains(@href,'after')]/@href").get()
        # if next_page is not None:
        #     # next_page = next_page.replace('before', 'after')
        #     yield response.follow(next_page, callback=self.parse)
