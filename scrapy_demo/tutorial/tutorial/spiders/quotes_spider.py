import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split('/')[-2]
    #     filename = 'quotes-{}.html'.format(page)

    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file {}'.format(filename))

    start_urls = [
        'http://lab.scrapyd.cn/page/1/'
    ]

    def parse(self, response):
        # page = response.url.split('/')[-2]
        # filename = 'quotes-{}.html'.format(page)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file {}'.format(filename))

        quote_list = response.css('div.quote')
        for i in quote_list:
            text = i.css('.text::text').extract_first()  # 名言
            autor = i.css('.author::text').extract_first()  # 作者
            tags = i.css('.tags .tag::text').extract()  # 标签列表
            tag = ','.join(tags)
            '''
            写入到文件
            '''
            fileName = '{}语录.txt'.format(autor)
            with open(fileName, 'a+') as f:
                t = '''
                {}
                标签: {}
                --------------
                '''.format(text, tag)
                f.write(t)
                f.close()

        next_page = response.css('.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
