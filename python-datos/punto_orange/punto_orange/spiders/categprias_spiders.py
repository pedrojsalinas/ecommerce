import scrapy


class CategoriasSpider(scrapy.Spider):
    name = "categorias"

    def start_requests(self):
        urls = [
            'https://puntoorange.com/categoria-producto/supermercado/almacen/aceites-y-vinagres/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for categoria in response.css('ul#menu-categorias-1 > li'):
            for producto in categoria.css('ul.sub-menu > li'):
                yield {
                    'categoria': categoria.css('a::text').get(),
                    'c_href': categoria.css('a::attr(href)').extract()[0],
                    'producto': producto.css('a::text').get(),
                    'p_href': producto.css('a::attr(href)').extract()[0],
                }
