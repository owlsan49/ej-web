# -*- coding: utf-8 -*-
# Copyright (c) 2022, Shang Luo
# All rights reserved.
# 
# Author: 罗尚
# Building Time: 2024/3/3
# Reference: None
# Description: None
from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import read_json

app = Flask(__name__)
CORS(app)


@app.route('/plus_one', methods=['GET'])
def push_words():
    results = {'resCode': 0}
    return jsonify(results)


if __name__ == '__main__':
    port = read_json('../config.json')['port']
    app.run(debug=True, port=port)
