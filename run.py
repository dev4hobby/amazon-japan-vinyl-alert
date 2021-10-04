from settings import DATABASES
from db import Mongo
from crawler import get_vinyl_document_list
from ifttt import send_vinyl_to_webhook

mongo = Mongo()
vinyls = get_vinyl_document_list()
for vinyl in vinyls:
    is_new = mongo.upsert_vinyl(vinyl)
    if is_new:
        send_vinyl_to_webhook(vinyl)
