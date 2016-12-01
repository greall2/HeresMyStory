#Ríona Greally - G00325504
#3rd Yr Software Development, GMIT
import couchdb
import time

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

#creating the database called 'stories'
db = couch.create('stories')

#formatting Date and Time 
currDate = time.strftime("%c")

#creating Documents in stories
doc ={'story': 'This is my First Story', 'Date': currDate}
doc1 ={'story': 'Three Irishmen, Paddy, Sean and Seamus, were stumbling home from the pub late one night and found themselves on the road which led past the old graveyard."Come have a look over here," says Paddy, "Its Michael O Gradys grave, God bless his soul. He lived to the ripe old age of 87." "That is nothing," says Sean, "here is one named Patrick O Toole, it says here that he was 95 when he died." Just then, Seamus yells out, "Good God, heres a fella that got to be 145!" "What was his name?" asks Paddy. Seamus stumbles around a bit, awkwardly lights a match to see what else is written on the stone marker and exclaims: "Miles, from Dublin." - Timmy K, Kerry', 'Date': currDate}


#saving the documents to database
db.save(doc)
db.save(doc1)