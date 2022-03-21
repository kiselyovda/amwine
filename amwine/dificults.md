# Пробелмы и их решения
1. Пройти верефикацию на возвраст - cookie
2. Установить город `Ростов на Дону` - cookie
``` python
   cookies = {
            'AMWINE__IS_ADULT': 'Y',
            'AMWINE__REGION_CODE': 'rostov-na-donu',
            'AMWINE__REGION_ELEMENT_XML_ID': '61',
            'AMWINE__REGION_ELEMENT_ID': '182688',
            'AMWINE__CITY_SALE_LOCATION_ID': '1249',
            'AMWINE__CITY_NAME': '%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83	'
        }
```
3. Каталог подгружается через `ajax` запросы

    > По сути ,большая часть данных лежит в `ajax` запросе и надо каким-то образом вытащить их оттуда.

`Ajax` запрос выглядит как в файле [test.json](test.json) или с отступами [test_expended.json](test_expended.json).

4. Цена не одинакова на всех карточках ⚠️ но в `ajax` она есть❗❗❗
