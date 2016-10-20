# -*- coding: utf-8 -*-
import scrapy


class BancosSpider(scrapy.Spider):
    name = "bancos"
    allowed_domains = ["http://www.buscabanco.org.br/AgenciasBancos.asp"]
    start_urls = (
        'http://www.buscabanco.org.br/AgenciasBancos.asp',
    )

    def parse(self, response):
        trs = response.xpath("//table[3]/tr/td/table/tr")
        trs = trs[1:len(trs) - 1]
        # trs_0_tds = trs[0].xpath("td")
        # name = trs_0_tds[1].xpath("a/text()").extract_first()
        # self.log(name)
        for tr in trs:
            tr_tds = tr.xpath("td")
            raw_name = tr_tds[1].xpath("a/text()").extract_first()
            raw_name = raw_name.rstrip()
            raw_name = raw_name.lstrip()
            yield {
                "name" : raw_name
            }

