import random
import time
import turtle

from tkinter import *
from tkinter import messagebox

delay=0.1
score=0
highscore=0

#snakebodies
bodies=[]

#GETTING scrren
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("grey")
s.setup(width=600,height=600)

#create head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white");
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#scoreboard
sb=turtle.Turtle()
sb.shape("square")
sb.color("black")
sb.penup()
sb.ht();
sb.goto(-250,-250)
sb.write("Score:0 | highscore :0")


sb1=turtle.Turtle()
def show():
    global sb1
    sb1.speed()
    sb1.shape("square")
    sb1.color("black")
    sb1.penup()
    sb1.ht()
    sb1.goto(-50,-250)
    sb1.write("Game Over ")
  
    

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
        head.direction="shop"

        #actual movements
        
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


def notify():
    
    global s
    global sb
    global delay
    global score
    global body
    global head
    global bodies
    ans=messagebox.askquestion("GAME OVER YES to continue ")
    if ans=='no':
        s.clear()
        s.bye()
    
#event handling -key mapping
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
#s.onkey(movestop,"space")

#main loop
while True:
    s.update()
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    # check collison with food
    if head.distance(food)<20:
        #move the foodto new random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #incr the len of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        #incr score
        score+=10

        #delay change
        delay-=0.001

        #update the highscore
        if score>highscore:
            highscore=score
        sb.clear()
        sb.write("Score:  {}  Highscore:  {}".format(score,highscore))

        
    #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #check collection with snake body
    for body in bodies:
        if body.distance(head)<20:
            show()
            time.sleep(1)
            sb1.clear()
            head.goto(0,0)
            head.direction="stop"
            
            notify()

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score=0
            delay=0.1

            #update score board
        
            

            sb.clear()
            sb.write("Score:  {}   Highscore:  {}".format(score,highscore))
           

    time.sleep(delay)
s.mainloop()
