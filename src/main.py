import ast
import json

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from justwatch import JustWatch

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "Chad Coders backend API"

@app.route('/getdata', methods=['GET'])
def get():
    just_watch = JustWatch(country='SE')
    results = just_watch.search_for_item(query=request.args.get('search'))
    items = results['items']
    with open('json_data.json', 'w') as outfile:
        json.dump(items, outfile)
    return jsonify(items)

@app.route('/show', methods=['GET'])
def getShow():
    just_watch = JustWatch(country='SE')
    results = just_watch.get_title(title_id=request.args.get('id'), content_type='show')
    with open('json_data.json', 'w') as outfile:
        json.dump(results, outfile)
    return jsonify(results)

@app.route('/movie', methods=['GET'])
def getMovie():
    just_watch = JustWatch(country='SE')
    results = just_watch.get_title(title_id=request.args.get('id'), content_type='movie')
    with open('json_data.json', 'w') as outfile:
        json.dump(results, outfile)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
