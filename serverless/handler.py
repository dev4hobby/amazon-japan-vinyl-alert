import json
import sys
from modules.db import Mongo
from modules.crawler import get_vinyl_document_list
from modules.ifttt import send_vinyl_to_webhook
from datetime import datetime
from modules.utils import parse_json

mongo = Mongo()

def crawl_vinyl_from_amazon_japan(event, context):
    vinyls = get_vinyl_document_list()
    for vinyl in vinyls:
        is_new = mongo.upsert_vinyl(vinyl)
        if is_new:
            send_vinyl_to_webhook(vinyl)


def get_vinyl_list(event, context):
    queryParams = event.get('queryStringParameters', None)
    when = datetime.now()
    try:
        if queryParams: 
            when = queryParams.get('when', None) \
                and datetime.strptime(queryParams['when'], '%Y%m%d_%H%M%S') \
                or datetime.now()
    except Exception as e:
        when = datetime.now()
    print(f'when: {when}')
    vinyls = mongo.get_vinyl_list(when)
    body = parse_json({
        "vinyls": vinyls,
        "last": len(vinyls)>0 and vinyls[-1].get('created_at') or None
    })
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
