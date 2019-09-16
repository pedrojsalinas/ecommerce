import scrapy
import json


class DescripcionSpider(scrapy.Spider):
    name = "descripcion"

    with open('productos.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    urls = []
    for i in obj:
        urls.append(i["href"])

    def start_requests(self):
        for url in self.urls:
            # urls = ['https://puntoorange.com/producto/pro-cat/',]
            # for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for producto in response.css('div.summary'):
            yield {
                'titulo': producto.css('h1::text').get(),
                'precio': float(producto.css('span.woocommerce-Price-amount::text').get()),
                'img': response.css('div.woocommerce-product-gallery__image img::attr(src)').extract()[0],
                'descripcion': response.css('div.woocommerce-Tabs-panel p::text').get(),
                'tipo': response.css('td.woocommerce-product-attributes-item__value p::text').get(),
                # 'stock': producto.css('p.stock in-stock::text').get(),
                'categoria': producto.css('span.posted_in a::text').get(),
                'marca': producto.css('span.yith-wcbr-brands a::text').get(),
            }
