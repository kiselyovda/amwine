# Парсинг карточки продукта
timestamp = `round(time.time())`

RPC = `response.css('div.catalog-element-info__article').css('span::text').get().split()[-1]`

URL = `response.url`

title = `response.css('h1::text').get().strip()`

marketing_tags = `response.css('span.tooltip_dk::text').get().strip()`

brand = `response.css('div.about-wine__block_params span.about-wine__param-value')[-3].css('a::text').get().strip()`

section = `[item.strip() for item in response.css('a.breadcrumbs__link::text').extract()]`


price_data:

    current = float(response.css('div.catalog-element-info__price.catalog-element-info__price_detail span::text').extract()[-4].replace(' ', '')) 
    original = float(response.css('div.catalog-element-info__price.catalog-element-info__price_detail span::text').extract()[-2].replace(' ', ''))
    sales_tag = f"Скидка {round((1 - response.css('div.catalog-element-info__price span::text').extract()[2] / response.css('div.catalog-element-info__price span::text').extract()[0]) * 100), 2)}%"

metadata:

    __description = response.css('div.about-wine__block p::text').get().strip()
    АРТИКУЛ = 
    СТРАНА ПРОИЗВОДИТЕЛЬ = [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value a::text').extract()][0]
    ПРОИЗВОДИТЕЛЬ = [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value a::text').extract()][1]
    ОБЪЕМ = [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value::text').extract()][2].replace(' ', '')
    КРЕПОСТЬ = [item.strip() for item in response.css('div.about-wine__block_params span.about-wine__param-value::text').extract()][-1].replace(' ', '')
    


assets:

    main_image = f"https://amwine.ru{response.css('div.catalog-element-info__picture img::attr(src)').get()}"
    set_images = отсутствуют доп картинки
    view360 = отсутствуют
    video = отсутствуют


variant = `на сайте есть варианты товара, но в карточке товара они отсутствуют`
