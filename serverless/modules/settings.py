from os import getenv, environ
from .utils import init_json_env

# if json env file is provided, use it
init_json_env(environ.get('CRAWLER_ENVIRONMENT', 'dev'))

DATABASES = {
    'host': getenv('VINYL_MONGO_HOST'),
    'port': getenv('VINYL_MONGO_PORT', 27017),
    'user': getenv('VINYL_MONGO_USER'),
    'password': getenv('VINYL_MONGO_PASSWORD'),
    'collection': getenv('VINYL_MONGO_COLLECTION', 'amazon_japan_lp')
}

CRAWLER = {
    'amazon_jp_url': 'https://amazon.co.jp',
    'amazon_jp_vinyl_url': 'https://www.amazon.co.jp/s?i=popular&bbn=561956&rh=n:561956,p_n_format_browse-bin:81877051&s=featured-rank&dc&language=en&qid=1633267955&rnid=81872051&ref=sr_st_featured-rank',
    'headers': {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'},
}

IFTTT = {
    'new_arrival_url': f"https://maker.ifttt.com/trigger/new_arrival_vinyl/with/key/{getenv('VINYL_IFTTT_WEBHOOK_KEY')}",
    'headers': {
        'Content-Type': 'application/json'
    }
}
