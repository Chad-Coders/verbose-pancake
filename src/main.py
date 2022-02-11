import ast
import json

import requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from justwatch import JustWatch

#print(results['items'])
#for x in results['items']:
#    print(x['title'])


app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return "Chad Coders backend API"

@app.route('/entertainment', methods=['GET'])
def get():
    my_dict = {"0": []}
    just_watch = JustWatch(country='SE')
    results = just_watch.search_for_item(query='avengers')
    items = results['items']
    with open('json_data.json', 'w') as outfile:
        json.dump(items, outfile)

    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
