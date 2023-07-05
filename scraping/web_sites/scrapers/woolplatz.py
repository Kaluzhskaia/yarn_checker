import requests
from bs4 import BeautifulSoup

from scraping.service.data_handler import update_or_create_items

SITE_URL = 'https://www.wollplatz.de/wolle'


def scrape_woolplatz():
    response = requests.get(SITE_URL)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(SITE_URL))

    soup = BeautifulSoup(response.text, 'html.parser')
    max_page = soup.find('span', id='ContentPlaceHolder1_lblPaginaVanTop').find_all('b')[1].text
    if not max_page:
        max_page = 1
    item_links = fetch_item_urls(max_page)
    fetched_data = fetch_item_details(item_links)
    update_or_create_items(fetched_data)


def fetch_item_urls(max_page):
    item_links = []
    for i in range(1, int(max_page) + 1):
        response = requests.get(f'{SITE_URL}?page={i}')
        if response.status_code != 200: continue
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('a', class_='productlist-imgholder gtm-product-impression')
        for item in items:
            if "/wolle/" in item['href']:
                item_links.append(item['href'])
    return item_links


def fetch_item_details(item_links):
    fetched_data = []
    for number, item_link in enumerate(item_links):
        response = requests.get(item_link)
        if response.status_code != 200: continue
        soup = BeautifulSoup(response.text, 'html.parser')

        params = item_link.split('/')
        brand = params[-2].replace('-', ' ').capitalize()

        name = params[-1].replace('-', ' ').capitalize()
        price = float(
            soup.find('span', class_='product-price').find('span', class_='product-price-amount').text.replace(',',
                                                                                                               '.'))

        stock_status = soup.find('div', id='ContentPlaceHolder1_upStockInfoDescription').decode_contents()
        available = "stock-green" in stock_status
        needle_size = soup.find(string="Nadelstärke")
        if needle_size:
            needle_size = needle_size.find_next('td').text
        composition = soup.find(string="Zusammenstellung")
        if composition:
            composition = composition.find_next('td').text

        GTIN = soup.find('span', itemprop='gtin')
        if GTIN:
            GTIN = GTIN.text
        item_dict = {
            'url': item_link,
            'brand': brand,
            'name': name,
            'price': price,
            'available': available,
            'needle_size': needle_size,
            'composition': composition,
            'GTIN': GTIN
        }
        fetched_data.append(item_dict)
    return fetched_data


scrape_woolplatz()
