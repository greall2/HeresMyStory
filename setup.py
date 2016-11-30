
import couchdb
import time

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

#creating the database called 'stories'
db = couch.create('stories')

#formatting Date and Time 
currDate = time.strftime("%c")

#creating Document in stories
doc ={'story': 'This is my Story', 'Date': currDate}

#saving the document to database
db.save(doc)