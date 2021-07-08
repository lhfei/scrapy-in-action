import scrapy

class WhiskySpider(scrapy.Spider):
    name = 'Whisky'
    start_urls = ['https://www.whiskyshop.com/']

    def parse(self, response, **kwargs):
        for product in response.css('div.product-item-info'):
            try:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': product.css('span.price::text').get(),
                    'link': product.css('a.product-item-link').attrib['href']
                }
            except:
               yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': product.css('a.product-item-link').attrib['href']
                } 
        # for title in response.css('div.product-item-info'):
        #     print(title)

        next_page = response.css('a.action.next').attrb['href']
        if next_page is not None:
            yield response.follow(next_page, callable=self.parse)
