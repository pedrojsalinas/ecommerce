import scrapy
import json


class ProductosSpider(scrapy.Spider):
    name = "productos"


    with open('categorias.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    urls = []
    for i in obj:
        urls.append(i["p_href"])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for producto in response.css('ul.products > li'):
            yield {
                'titulo': producto.css('h2::text').get(),
                'precio': float(producto.css('span.woocommerce-Price-amount::text').get()),
                'href': producto.css('a::attr(href)').extract()[0],
                'img': producto.css('img::attr(src)').extract()[0],
            }
