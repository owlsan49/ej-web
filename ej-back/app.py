# -*- coding: utf-8 -*-
# Copyright (c) 2022, Shang Luo
# All rights reserved.
# 
# Author: 罗尚
# Building Time: 2024/3/3
# Reference: None
# Description: None
import base64
from flask import Flask, jsonify, send_file
from flask_cors import CORS
from utils import (read_json, ej_recorder, jot_plus, plot_jog,
                   recommend_day)

app = Flask(__name__)
CORS(app)


@app.route('/plus_one', methods=['GET'])
def plus_one():
    results = {'resCode': 0}
    jot_plus(ej_recorder)
    plot_jog(ej_recorder)
    return jsonify(results)


@app.route('/get_obj', methods=['GET'])
def get_obj():
    results = {'resCode': 0}
    results['img_path'] = '/get_plot'
    results['info'] = recommend_day(ej_recorder)
    return jsonify(results)


@app.route('/get_plot', methods=['GET'])
def get_plot():
    return send_file("plot.png", mimetype='image/png')


if __name__ == '__main__':
    port = read_json('../config.json')['port']
    app.run(debug=True, port=port)
