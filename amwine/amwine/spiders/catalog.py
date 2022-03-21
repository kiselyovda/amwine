from email import header
import time
import scrapy

current_time = round(time.time())

class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['amwine.ru']
    start_urls = ['https://amwine.ru/catalog/krepkie_napitki/viski/ancnoc-12-yo/']


    def start_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36'
            }
        cookies = {
                    'AMWINE__IS_ADULT': 'Y',
                    'AMWINE__REGION_CODE': 'rostov-na-donu',
                    'AMWINE__REGION_ELEMENT_XML_ID': '61',
                    'AMWINE__REGION_ELEMENT_ID': '182688',
                    'AMWINE__CITY_SALE_LOCATION_ID': '1249',
<<<<<<< HEAD
                    'AMWINE__CITY_NAME': '%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83	'
                    },
        for url in self.start_urls:
            
            yield scrapy.Request(
                url,
                cookies=cookies,
                headers=headers,
=======
                    'AMWINE__CITY_NAME': '%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83	',
                    },
>>>>>>> 6a2f8aa9dcf52ce4fedec2de93c82aff2a9e8987
                callback=self.parse_product
                )


    def parse_product(self, response, **kwargs):
        yield {
            'timestamp': current_time,
            'RPC': response.css('div.catalog-element-info__article').css('span::text').get().split()[-1],
            'URL': response.url,
            'title' : response.css('h1::text').get().strip(),
            'marketing_tags': response.css('span.tooltip_dk::text').get(),
            'brand': response.css('div.about-wine__block_params span.about-wine__param-value a::text')[1].get().strip(),
            'section': [item.strip() for item in response.css('a.breadcrumbs__link::text').extract()],
            'price_data': {
                'current': response.css('div.catalog-element-info__price span::text').extract()[0],
                'original': response.css('div.catalog-element-info__price span::text').extract()[2],
                # 'sales_tag': f"Скидка {round((1 - float(response.css('div.catalog-element-info__price span::text').extract()[0].replace(' ', '')) / float(response.css('div.catalog-element-info__price span::text').extract()[2].replace(' ', ''))) * 100, 2)}%",
            },
            'metadata': {
                '__description': response.css('div.about-wine__block p::text').get().strip().replace('\"', ''),
                'АРТИКУЛ': response.css('div.catalog-element-info__article').css('span::text').get().split()[-1],
                'СТРАНА ПРОИЗВОДИТЕЛЬ': [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value a::text').extract()][0],
                'ПРОИЗВОДИТЕЛЬ': [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value a::text').extract()][1],
                'ОБЪЕМ': [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value::text').extract()][2].replace(' ', ''),
               'КРЕПОСТЬ': [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value::text').extract()][-1].replace(' ', ''),
            },
            'assets': {
                'main_image': f"https://amwine.ru{response.css('div.catalog-element-info__picture img::attr(src)').get()}",
                'set_images': [''],
                'view360': [''],
                'video': [''],
            },
            'variant': 1
        }
