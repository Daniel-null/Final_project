from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request, redirect, url_for, request, json, jsonify, current_app as app
# for prez change this to sense_emu
from sense_hat import SenseHat
from sense_hat import stick
from datetime import date
from time import clock, sleep
import requests
import sqlite3 
from random import randint
#importing the class that hold the game designs 
from designs import Dog
from time import sleep 
import threading
import time

#this import allows us to read and call other scripts not in the same directory
import sys
#this allows python to actually read another directory for scripts
sys.path.insert(0, '~/Desktop/Final/machineAI') #note you have to create a blank python file called __init__. This tells python that its a package it can import 
#sys imported scripts from the machine ai folder
from machineAI import voice

D_UP = stick.DIRECTION_UP
D_DOWN = stick.DIRECTION_DOWN
D_LEFT = stick.DIRECTION_LEFT
D_RIGHT = stick.DIRECTION_RIGHT
direction = D_RIGHT

sense = SenseHat()
#variables for the game 
dog = Dog ()
#list to use for the condition that the player jumps at the appropriate time

app = Flask(__name__)

#time while function
def counter():
    global clockT
    clockT = 0
    while clockT:
        clockT += 1
        time.sleep(1)
        print(clockT)

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
    
    # store game score in a score variable
    score = 0 #<<<<<<<<< placeholder 0
    #these lists 
    obMove = [dog.obStage1, dog.obStage2, dog.obStage3]
    upDog = [dog.overOb1, dog.overOb2,dog.overOb3,dog.overOb4,dog.lastOver,dog.up,dog.neutral]
    gameRunTime = True  
    level = 1 
    lastPixels = []
    delay = 1
    global direction

    #add functions for game in this route 
    #return redirect(url_for('data', user=user, today=today, score=score))
         
    def respond_to_voice(command):
        print(command)
        label = command[0]
        global direction
        if command[0] == 'go_up':
            direction = D_UP
            print(direction)
        elif command[0] == 'go_down':
            direction = D_DOWN
            print(direction)
        elif command[0] == 'go_left':
            direction = D_LEFT
            print(direction)
        elif command[0] == 'go_right':
            direction = D_RIGHT
            print(direction)

    def joystick(event):
        global direction        
        if event.direction == D_RIGHT:
            direction = D_RIGHT
            print(direction)
        elif event.direction == D_UP:
            #the position of the dog will be up
            direction = D_UP
            print(direction)
        elif event.direction == D_DOWN:
            #the dog will then come down
            direction = D_DOWN
            print(direction)
        elif event.direction == D_LEFT:
            direction = D_LEFT
            print(direction)

    sense.stick.direction_any = joystick


    sense.show_message("Level 1")  
    sense.set_pixels(dog.neutral)
    sleep(1)

    count_thread = threading.Thread(target=counter)
    count_thread.start()

    while gameRunTime:
        command = listener.next(block=False)
        if command:
            print(command)
            respond_to_voice(command)
            print(direction)

        # LEVEL 1  
        for i in range(len(obMove)): 
            sense.set_pixels(obMove[i])
            sleep(delay)
            lastPixels = obMove[i]
            command = listener.next(block=False)
            if command:
                print(command)
                respond_to_voice(command)
                print(direction)

            if not gameRunTime:
                break
        if direction == D_UP:
            direction = D_DOWN
            for i in range(len(upDog)):
                sense.set_pixels(upDog[i]) 
                sleep(delay)
                lastPixels = upDog[i]
            score +=1
            print(score)
        # if the user jumps over 3 obstacles, the level increases
        #UP LEVELLLLL
        if score % 3 == 0 and lastPixels == dog.neutral: 
                level +=1
                sense.show_message("Level " + str(level))
                delay *= 0.25
        # need the else condition to hanlde:
        # if the sense.set_pixels == dog.obStage3 and direction != D_UP
        elif lastPixels == obMove[2] and direction != D_UP:
            gameRunTime = False
        print(gameRunTime)
        
    sense.set_pixels(dog.gameOver)
    sleep(2)
    sense.show_message("You Lost!")
                
    return redirect(url_for('data', user=user, today=today, score=score))



if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
