from sqlite3.dbapi2 import Cursor
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

@app.route('/data/<user>/<score>', methods = ['POST', 'GET'])
def data(user, score):
    #opens the database
    conn = sqlite3.connect('./static/data/score.db')
    Curs = conn.cursor()
    #executes the command to pass username and score
    Curs.execute("INSERT INTO task (user, score) VALUES((?),(?))", (user, score))
    conn.commit ()
    #closes database
    conn.close
    
    return redirect(url_for('all'))