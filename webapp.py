#Ríona Greally - G00325504
#3rd Yr Software Development, GMIT
import couchdb
import json
from flask import Flask, render_template
from flask import request
import time

import flask as fl

app = fl.Flask(__name__)

# Adapted from https://pythonhosted.org/CouchDB/getting-started.html
couch = couchdb.Server("http://127.0.0.1:5984/")

#calling an existimg database
db = couch['stories'] # existing Database

#Routing adapted from http://flask.pocoo.org/docs/0.11/quickstart/#routing
@app.route("/")
def route():
	return render_template("index.html")
	

@app.route('/postStory', methods=['GET','POST'])
def story():
	story = fl.request.values["story"]
	string = 'Your Post has been added to Stories!' 

	#Time and Date adapted from https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
	currDate = time.strftime("%c")
	doc = {"story": story, "Date": currDate}
	db.save(doc)
	return string


#routing to the About page
@app.route("/about")
def about():
	return render_template("about.html")

#routing to the Stories Page
@app.route("/stories")
def stories():
	# Adapted from http://stackoverflow.com/questions/1640054/multiple-couchdb-document-fetch-with-couchdb-python
	rows = db.view('_all_docs', include_docs = True)
	docs = [row.doc for row in rows]
	post = json.dumps((docs))
	poster = json.loads(post)
	poster.reverse()
	return render_template("stories.html", storys = poster)


if __name__ == "__main__":
	app.run()


