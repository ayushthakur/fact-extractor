from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
from spacy import displacy
import wikipedia
import textacy.extract
#import en_core_web_sm
nlp = spacy.load('en_core_web_lg')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        #topic = request.form['topic']
        doc = nlp(wikipedia.page(rawtext).content)

        # Extract semi-structured statements
        statements = textacy.extract.semistructured_statements(doc, rawtext)
        results = []
        for statement in statements:
            subject, verb, fact = statement
            results.append(fact)
    return render_template("index.html",results=results,num_of_results = len(results))


if __name__ == '__main__':
	app.run(debug=True)
