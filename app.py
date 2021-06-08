from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request, redirect, url_for, request, json, jsonify, current_app as app
from sense_hat import SenseHat
from datetime import date
import requests
import sqlite3 
#importing the class that hold the game designs 
from designs import Dog

#this import allows us to read and call other scripts not in the same directory
import sys
#this allows python to actually read another directory for scripts
sys.path.insert(0, '~/Desktop/Final/machineAI') #note you have to create a blank python file called __init__. This tells python that its a package it can import 
#sys imported scripts from the machine ai folder
from machineAI import voice

sense = SenseHat()
#variables for the game 
dog = Dog ()
gameRunTime = True  
level = 0 

app = Flask(__name__)

@app.route('/')
def info():
    return redirect(url_for('all'))

@app.route('/all', methods=(['GET', 'POST']))
def all():
    if request.method =='POST':
        #create html form to get user
        user = request.form['user']
        #time will be stored in a variable
        today = str(date.today())
        #the user and date is passed to the game
        return redirect(url_for('game', user = user, today=today))
    else:
        #will call for scores, names, and maybe dates and pass it to the website.
        conn = sqlite3.connect('./static/data/score.db')
        curs = conn.cursor()
        scores = []
        rows = curs.execute("SELECT * FROM score ORDER BY score DESC")
        for row in rows:
            score = ({'user':row[1], 'score':row[2], 'date':row[3]})
            scores.append(score)
        return render_template('index.html', scores = scores)

@app.route('/data/<user>/<today>/<score>', methods = ['POST', 'GET'])
def data(user, today, score):
    #opens the database
    conn = sqlite3.connect('./static/data/score.db')
    Curs = conn.cursor()
    #executes the command to pass username and score
    Curs.execute("INSERT INTO score (user, score, date) VALUES((?),(?),(?))", (user, score, today))
    conn.commit()
    #closes database
    conn.close
    
    return redirect(url_for('all'))

@app.route('/game/<user>/<today>', methods=(['GET', 'POST']))
def game(user, today):
    listener = voice.AudioClassifier(model_file=voice.VOICE_MODEL, 
                                        labels_file=voice.VOICE_LABELS,
                                            audio_device_index=2)
    #we can call the game from here 
    # store game score in a score variable
    score = 0 #<<<<<<<<< placeholder 0

    #add functions for game in this route 
    return redirect(url_for('data', user=user, today=today, score=score))
while(gameRunTime == True):
    #code for the game 
    sense.setpixels("Game start")
    level += 1 
    if(level == 1):
        sense.setpixels(dog.neutral)
        sleep(2)
        


#if(gameRunTime == False):
#   sense.setpixels("Game Over")
if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')