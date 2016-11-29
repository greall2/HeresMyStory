import couchdb
import json
from flask import Flask, render_template
from flask import request

import flask as fl

app = fl.Flask(__name__)

couch = couchdb.Server("http://127.0.0.1:5984/")

#db = couch.create('test')

db = couch['test']


@app.route("/")
def route():
	return render_template("index.html")
	

@app.route('/postStory', methods=['GET','POST'])
def fname():
	story = fl.request.values["story"]
	#return 'Your name is '  + name
	string = 'Your Post: ' + story
	doc = {"story": story}
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


