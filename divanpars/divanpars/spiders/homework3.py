# 3 Задача. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divanparscraper"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/divany-i-kresla"]

    def __init__(self, *args, **kwargs):
        super(DivannewparsSpider, self).__init__(*args, **kwargs)
        self.crawled_data = []

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            if price:
                price = int(price.replace(' ', '').replace('₽', ''))  # Удаляем пробелы и символ рубля
            self.crawled_data.append({'name': name, 'price': price})
            yield {
                'name': name,
                'price': price,
            }

    def close(self, reason):
        with open("divanscraper.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Название дивана", "Цена"])
            for item in self.crawled_data:
                writer.writerow([item['name'], item['price']])