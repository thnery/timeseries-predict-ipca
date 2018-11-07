#!/usr/bin/env python

import scrapy
import csv

class IPCASpider(scrapy.Spider):
    name = 'ipcaspider'
    start_urls = ['http://www.debit.com.br/consulta30.php?indice=ipca']

    def parse(self, response):
        ipca_indexes = list()
        for item in response.css('.listagem > tbody > tr'):
            obj = { 'year_month': item.css('.ta-left ::text').extract_first(),
                    'ipca': item.css('.ta-right ::text').extract_first() }

            ipca_indexes.append(obj)

        with open('./ipca.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for idx in ipca_indexes:
                print(idx)
                ym = idx['year_month'].split("/")
                timestamp = "{}-{}".format(ym[1], ym[0])
                line = [timestamp, idx['ipca'].replace(",", ".")]
                print(line)
                writer.writerow(line)
