import couchdb
import json
from flask import Flask, render_template
from flask import request
import time

import flask as fl

app = fl.Flask(__name__)

# Adapted from https://pythonhosted.org/CouchDB/getting-started.html
couch = couchdb.Server("http://127.0.0.1:5984/")

#db = couch.create('test')

db = couch['test'] # existing Database


@app.route("/")
def route():
	return render_template("index.html")
	

@app.route('/postStory', methods=['GET','POST'])
def fname():
	story = fl.request.values["story"]
	string = 'Your Post: ' + story
	
	#Time and Date adapted from https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
	currDate = time.strftime("%c")
	doc = {"story": story, "Date": currDate}
	db.save(doc)
	return string


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/stories")
def stories():
	rows = db.view('_all_docs', include_docs = True)
	docs = [row.doc for row in rows]
	test = json.dumps((docs),indent = 2)
	tester = json.loads(test)
	tester.reverse()
	return render_template("stories.html", storys = tester)


if __name__ == "__main__":
	app.run()


