from serverless.modules import db, crawler, ifttt

mongo = db.Mongo()
vinyls = crawler.get_vinyl_document_list()
for vinyl in vinyls:
    is_new = mongo.upsert_vinyl(vinyl)
    if is_new:
        ifttt.send_vinyl_to_webhook(vinyl)
