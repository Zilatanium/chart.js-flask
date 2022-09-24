# first install requests: sudo pip3 install requests
from flask import Flask, render_template
import requests
import sys
import json
import random

app = Flask(__name__)

@app.route('/plot_line', methods=["GET"])
def plot():
    xValues = [1,2,3,4,5,6,7,8,9,10]
    yValues=[]
    for x in range(10):
        yValues.append(random.randint(1,20))
    return render_template('plot.html', xValues = json.dumps(xValues), yValues = json.dumps(yValues))