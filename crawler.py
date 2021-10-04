import requests
from settings import CRAWLER
from bs4 import BeautifulSoup

def get_vinyl_document_list() -> list:
    data = requests.get(CRAWLER.get('amazon_jp_vinyl_url'), headers=CRAWLER.get('headers'))
    soup = BeautifulSoup(data.text, 'html.parser')
    vinyls = soup.select('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div')
    documents = list()
    for vinyl in vinyls:
        try:
            vinyl_info = {
                'title': vinyl.select_one('span.a-text-normal').text,
                'price': vinyl.select_one('span.a-price-whole').text,
                'cover': vinyl.select_one('img.s-image').get('src'),
                'url': f"{CRAWLER.get('amazon_jp_url')}{vinyl.select_one('a').get('href')}",
                'artist': vinyl.select_one('a.a-size-base.a-link-normal').text 
                    if vinyl.select_one('a.a-size-base.a-link-normal').text != 'Vinyl'
                    else vinyl.select_one('div.a-row.a-size-base.a-color-secondary').text.replace('by ', '')
            }
            documents.append(vinyl_info)
        except Exception as e:
            # 불필요한 div를 거르기위한 트릭
            pass
    return documents
