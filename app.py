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

@app.route('/all', methods=(['GET', 'POST']))
def all():
    if request.method =='POST':
        user = request.form['user']
        #we could add a date date = request.form['date']
        return redirect(url_for('game', user = user))
    else:
        #will call for scores, names, and maybe dates and pass it to the website.
        conn = sqlite3.connect('./static/data/score.db')
        curs = conn.cursor()
        scores = []
        rows = curs.execute("SELECT * FROM score")
        for row in rows:
            score = ({'user':row[1], 'score':row[2]})
            scores.append(score)
        return render_template('index.html', scores = scores)

@app.route('/data/<user>/<score>', methods = ['POST', 'GET'])
def data(user, score):
    #opens the database
    conn = sqlite3.connect('./static/data/score.db')
    Curs = conn.cursor()
    #executes the command to pass username and score
    Curs.execute("INSERT INTO task (user, score) VALUES((?),(?))", (user, score))
    conn.commit()
    #closes database
    conn.close
    
    return redirect(url_for('all'))

@app.route('/game/<user>', methods=(['GET', 'POST']))
def game(user):
    #we can call the game from here
    # store game score in a score variable
    score = 0 #<<<<<<<<< placeholder 0
    return redirect(url_for('data', user=user, score=score))

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')