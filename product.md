timestamp = `round(time.time())`

RPC = `response.css('div.catalog-element-info__article').css('span::text').get().split()[-1]`

title = `response.css('h1::text').get().strip()`

marketing_tags = `response.css('span.tooltip_dk::text').get().strip()`

brand = `response.css('div.about-wine__block_params span')[-3].css('a::text').get().strip()`

section = `[item.strip() for item in response.css('a.breadcrumbs__link::text').extract()]`


price = `response.css('div.catalog-element-info__price span::text')[-2].get()`

metadata:

    __description = `response.css('div.about-wine__block p::text').get().strip()`

assets:

    main_image = f"https://amwine.ru{response.css('div.catalog-element-info__picture img::attr(src)').get()}"
    set_images = отсутствуют доп картинки
    view360 = отсутствуют
    video = отсутствуют


variant = `на сайте есть варианты товара, но в карточке товара они отсутствуют`
