import couchdb
import time

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch.create('stories')
currDate = time.strftime("%c")
doc ={'story': 'This is my Story', 'Date': currDate}
db.save(doc)