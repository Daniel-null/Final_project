from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#colors for the turtle 
r = (255, 0, 0)
c = (0, 255, 255)
db = (255, 128, 0)
br = (141, 85, 36)
l = (128, 255, 128)
w = (255,255,255)
d = (255,0, 128)

class Dog: 
    neutral = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, db, br,br,c, c, c,
    br, c, db, br, w, c,c,c, 
    c, br, r, r,br,c,c, c, 
    c, br, br,br,c,c,c, c,
    c, br, c, br,c,c,c, c, 
    l, l, l, l, l, l, l, l 
    ]
    obStage1 = [
    c, c, c, c, c, c, c, c,  
    c, c, c, c, c, c, c, c,   
    c, c, db, br, br, c, c, c, 
    br, c, db, br, w, c, c, c, 
    c, br, r, r, br, c, c, c, 
    c, br, br, br, c, c, c, d, 
    c, br, c, br, c, c, c, d, 
    l, l, l, l, l, l, l, l 
    ]
    obStage2 = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c, 
    c, c, db, br, br, c, c,c, 
    br, c, db, br, w, c,c,c, 
    c, br, r, r, br,c, c,c, 
    c, br, br, br, c, c, d,d, 
    c, br, c, br, c, c, d, d, 
    l, l, l, l, l, l, l, l 
    ]
    obStage3 = [
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, db, br, br, c, c, c, 
    br, c, db, br, w, c, c, c, 
    c, br, r, r, br, c, c, c, 
    c, br, br, br, c, r, r, c, 
    c, br, c, br, c, r, r, c, 
    l, l, l, l, l, l, l, l 
    ]
    overOb1 = [
    c, c, db, br, br, c, c, c, 
    br, c, db, br, w, c, c, c, 
    c, br, r, r, br, c, c, c, 
    c, br, br, br, c, c, c, c, 
    c, br, c, br, c, c, c, c, 
    c, c, c, d, d, c, c, c, 
    c, c, c, d, d, c, c, c, 
    l, l, l, l, l, l, l, l 
    ]
    overOb2 = [
    c, c, db, br, br, c, c, c,
    br, c, db, br, w, c, c, c,
    c, br, r, r, br, c, c, c,
    c, br, br, br, c, c, c, c,
    c, br, c, br, c, c, c, c,
    c, c, d, d, c, c, c, c,
    c, c, d, d, c, c, c, c,
    l, l, l, l, l, l, l, l
    ]
    overOb3 = [
    c, c, db, br, br, c, c, c,
    br, c, db, br, w, c, c, c,
    c, br, r, r, br, c, c, c,
    c, br, br, br, c, c, c, c,
    c, br, c, br, c, c, c, c,
    c, d, d, c, c, c, c, c,
    c, d, d, c, c, c, c, c,
    l, l, l, l, l, l, l, l
    ]
    overOb4 = [
    c, c, db, br, br, c, c, c,
    br, c, db, br, w, c, c, c,
    c, br, r, r, br, c, c, c,
    c, br, br, br, c, c, c, c,
    c, br, c, br, c, c, c, c,
    d, d, c, c, c, c, c, c,
    d, d, c, c, c, c, c, c,
    l, l, l, l, l, l, l, l
    ] 
    lastOver = [
    c, c, db, br, br, c, c, c,
    br, c, db, br, w, c, c, c,
    c, br, r, r, br, c, c, c,
    c, br, br, br, c, c, c, c,
    c, br, c, br, c, c, c, c,
    d, c, c, c, c, c, c, c,
    d, c, c, c, c, c, c, c,
    l, l, l, l, l, l, l, l	
	]
    up = [
    c, c, db, br, br, c, c, c,
    br, c, db, br, w, c, c, c,
    c, br, r, r, br, c, c, c,
    c, br, br, br, c, c, c, c,
    c, br, c, br, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    l, l, l, l, l, l, l, l
    ]
    gameOver = [
    c, c, c, c, c, c, c, c, 
    c, c, c, c, c, c, c, c, 
    c, c, db, br, br, c, c, c, 
    br, c, db, br, w, c, c, c, 
    c, br, r, r, br, c, c, c, 
    c, br, br, br, d, d, c, c, 
    c, br, c, br, d, d, c, c, 
    l, l, l, l, l, l, l, l 
    ]




