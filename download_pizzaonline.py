import re
from traceback import print_exc

import requests
import bs4
import json


city_links = [
    url.replace('#lista', '') for url in (
    a.get('href') for a in bs4.BeautifulSoup(
        requests.get('https://pizza-online.fi/ravintolat/').text,
        "html.parser"
    ).find_all('a')
    )
    if re.match(r'^/ravintolat/([^/]+)$', url)
]

restaurant_data = []

for i, city_link in enumerate(city_links, 1):
    print('%3d/%-3d: %s' % (i, len(city_links), city_link))
    content = requests.get('https://pizza-online.fi/%s' % city_link).text
    try:
        restaurants_line = re.search(r'var restaurants = (.+);$', content, re.MULTILINE)
        restaurant_data.extend(json.loads(restaurants_line.group(1)))
    except:
        print('extraction failed')
        print_exc()


with open('pizza-online.json', 'w', encoding='utf-8') as outf:
    json.dump(restaurant_data, outf, ensure_ascii=False, indent=4)
