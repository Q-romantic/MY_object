# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/16  016 下午 13:15
@Author  : Jan
@File    : test.py
"""

""" {} """

from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {'id': 0, 'name': 'AA', 'num': 0},
    {'id': 1, 'name': 'BB', 'num': 0},
    {'id': 2, 'name': 'CC', 'num': 0},
]

@app.route('/')
def login():
    return render_template('login.html', data=data)

@app.route('/index')
def index():
    uname = request.args.get('uname')
    pwd = request.args.get('pwd')
    return render_template('index.html', data=data)

@app.route('/dianzan')
def dianzan():
    id = request.args.get('id')
    data[int(id)]['num'] += 1
    return index()





app.run(debug=True)
























































