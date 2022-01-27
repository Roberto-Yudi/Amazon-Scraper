import scrapy
import pandas as pd

name_list= []
price_list = []


class IphoneSpider(scrapy.Spider):
    page_num = 2

    name = 'BPA'
    start_urls = ['https://www.amazon.com/s?k=iphone&crid=TR0BSYSHDX0Y&sprefix=ip%2Caps%2C448&ref=nb_sb_noss_2']

    def parse(self, response):


        for product in response.css("[class='a-section']"):
            name = product.css("[class='a-size-medium a-color-base a-text-normal']::text").get()
            price = product.css("[class='a-offscreen']::text").get()

            print(name)
            print(price)

            name_list.append(name)
            price_list.append(price)
        
        next_page = f'https://www.amazon.com/s?k=iphone&page={IphoneSpider.page_num}&qid=1643225109&ref=sr_pg_{IphoneSpider.page_num}'

        if IphoneSpider.page_num < 6:
            IphoneSpider.page_num += 1
            print(IphoneSpider.page_num)
            yield response.follow(next_page, callback=self.parse)

        df = pd.DataFrame({
            'name': name_list,
            'price': price_list
        })

        df.to_excel('iphone.xlsx')