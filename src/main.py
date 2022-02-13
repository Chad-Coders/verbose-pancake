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

@app.route('/entertainment', methods=['GET'])
def get():
    just_watch = JustWatch(country='US')
    results = just_watch.search_for_item(query=request.args.get('search'))
    items = results['items']
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
