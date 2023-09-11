from typing import List, Dict

import requests
from bs4 import BeautifulSoup

from scraping.service.data_handler import update_or_create_items

SITE_URL = 'https://www.wollplatz.de/wolle'


def scrape_woolplatz():
    """Main function to scrape WoolPlatz website."""
    response = requests.get(SITE_URL)
    if response.status_code != 200:
        raise Exception(f'Failed to load page {SITE_URL}')

    soup = BeautifulSoup(response.text, 'html.parser')
    max_page = soup.find('span', id='ContentPlaceHolder1_lblPaginaVanTop').find_all('b')[1].text
    max_page = int(max_page) if max_page else 1

    item_links = fetch_item_urls(max_page)
    fetched_data = fetch_item_details(item_links)
    print(f"Fetched {len(fetched_data)} items")
    print(fetched_data)
    update_or_create_items(fetched_data)


def fetch_item_urls(max_page):
    """Fetch all item URLs across multiple pages."""
    item_links = []
    for i in range(1, max_page + 1):
        print(f"Fetching page {i} of {max_page}")
        response = requests.get(f'{SITE_URL}?page={i}')
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('a', class_='productlist-imgholder gtm-product-impression')

        item_links.extend([
            item['href'] for item in items if "/wolle/" in item['href']
        ])

    return item_links


def fetch_item_details(item_links: List[str]) -> List[Dict]:
    """Fetch details of each individual item."""
    fetched_data = []

    for number, item_link in enumerate(item_links):
        print(f"Fetching item {number + 1} of {len(item_links)}")
        response = requests.get(item_link)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        fetched_data.append(extract_item_details(soup, item_link))

    return fetched_data


def extract_item_details(soup: BeautifulSoup, item_link: str) -> Dict:
    """Extract details from the soup object."""
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

    gtin = soup.find('span', itemprop='gtin')
    if gtin: gtin = gtin.text
    return {
        'url': item_link,
        'brand': brand,
        'name': name,
        'price': price,
        'available': available,
        'needle_size': needle_size,
        'composition': composition,
        'GTIN': gtin
    }


scrape_woolplatz()
