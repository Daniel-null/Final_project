from flask import Flask, render_template, request, redirect, url_for, request, json, jsonify, current_app as app
from sense_hat import SenseHat
import requests
import sys
import sqlite3 

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def info():
    return redirect(url_for('all'))

@app.route('/all', methoods=(['GET', 'POST']))
def all():
    if request.method =='POST':
        return 0
    else:
        return 0

