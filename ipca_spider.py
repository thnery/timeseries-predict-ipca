#!/usr/bin/env python

import scrapy

class IPCASpider(scrapy.Spider):
    name = 'ipcaspider'
    start_urls = ['http://www.debit.com.br/consulta30.php?indice=ipca']

    def parse(self, response):
        for item in response.css('.listagem .zb'):
            obj = { 'yeah_month': item.css('.ta-left ::text').extract_first(),
                    'ipca': item.css('.ta-right ::text').extract_first() }

            yield obj
            # TODO write CSV
