import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yarn_checker.settings')

django.setup()
from scraping.models import YarnProduct, WebResource


def update_or_create_items(item_dict):
    for item in item_dict:
        yarn_product, created = YarnProduct.objects.update_or_create(
            GTIN=item['GTIN'],
            name=item['name'],
            brand=item['brand'],
            needle_size=item['needle_size'],
            composition=item['composition'],
        )
        yarn_product.save()
        WebResource.objects.update_or_create(
            yarn_product=yarn_product,
            url=item['url'],
            current_price=item['price'],
            available=item['available'],
        )
        print(f"Updated {yarn_product.name} from {yarn_product.brand} with GTIN {yarn_product.GTIN}")
        calibrate_prices(yarn_product)


def calibrate_prices(yarn_product):
    resources = yarn_product.resources.all()
    prices = [resource.current_price for resource in resources]
    lowest_price = min(prices)
    yarn_product.lowest_price = lowest_price
    if yarn_product.historical_lowest_price is None or yarn_product.historical_lowest_price > lowest_price:
        yarn_product.historical_lowest_price = lowest_price
    yarn_product.save()
    print(
        f"Updated price {yarn_product.name} from {yarn_product.brand}, current lowest price: {yarn_product.lowest_price}")
