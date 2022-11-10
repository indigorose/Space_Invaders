# ---- Main Imports ---- #
import turtle
from turtle import *
import math
import random


# ---- Class Imports ---- #
# from ship import Ship
# from missile import Missile
# from invader import Invaders
# from scoreboard import Scoreboard


# ---- Screen Setup ---- #
screen = Screen()
screen.setup(width=700, height=800)
screen.bgcolor('black')
screen.bgpic('./Images/Background.gif')
screen.title("Space Invaders")

# ---- Game Icons ---- #
turtle.register_shape('./Images/invader.gif')
turtle.register_shape('./Images/player.gif')

# ---- Border ---- #
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# ---- Player's Ship ---- #
ship = turtle.Turtle()
ship.shape("./Images/player.gif")
ship.penup()
ship.speed(0)
ship.setposition(0, -250)
ship.setheading(90)
shipspeed = 20

# ---- Ship's Missile ---- #
missile = turtle.Turtle()
missile.color("white")
missile.shape("circle")
missile.penup()
missile.speed(0)
missile.setheading(90)
missile.shapesize(0.5, 0.5)
missile.hideturtle()
missilespeed = 40
missilestate = 'ready'


# ---- Ship Functionality ---- #
def move_left():
    x = ship.xcor()
    x -= shipspeed
    if x < -280:
        x = -280
    ship.setx(x)


def move_right():
    x = ship.xcor()
    x += shipspeed
    if x > 280:
        x = 280
    ship.setx(x)


# ---- Missile Functionality ---- #
def fire_missile():
    global missilestate
    if missilestate == 'ready':
        missilestate = "fire"
        # Move the missile to just above the ship
        x = ship.xcor()
        y = ship.ycor() + 10
        missile.setposition(x, y)
        missile.showturtle()


# ---- Invaders ---- #
# invaders = Invaders()
number_of_invaders = 10
invaders = []

for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())
for invader in invaders:
    invader.shape("./Images/invader.gif")
    invader.penup()
    invader.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    invader.setposition(x, y)
invaderspeed = 5


# ---- Collision Detection ---- #
def isCollision_invader_missile(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


def isCollision_invader_player(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False


# ---- Key Listening ---- #
turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_missile, "space")

# ---- Scoreboard ---- #
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('purple')
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "SCORE: %s" % score
score_pen.write(scorestring, False, align='left', font=('Arial', 18, "normal"))
score_pen.hideturtle()

# ---- Game Play ---- #
# scoreboard = Scoreboard()
game_is_on = False
missed_invaders = 0
while True:
    for invader in invaders:
        # Move the invaders across the screen
        x = invader.xcor()
        x += invaderspeed
        invader.setx(x)
        # Move the invader back and down
        if invader.xcor() > 270:
            # Move all the invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
                if i.ycor() < -285 and game_is_on is False:
                    i.hideturtle()
                    missed_invaders += 1
                    if missed_invaders == 5:
                        game_is_on = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    i.setposition(x, y)
                    i.showturtle()
            # Change invader direction
            invaderspeed *= -1

        if invader.xcor() < -270:
            # Move all invaders down
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
                if i.ycor() < -285 and game_is_on is False:
                    i.hideturtle()
                    missed_invaders += 1
                    if missed_invaders == 5:
                        game_is_on = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    i.setposition(x, y)
                    i.showturtle()
            # Change invader direction
            invaderspeed *= -1

        # Check for collision between the missile and the enemy
        if isCollision_invader_missile(missile, invader):
            # Reset the missile
            missile.hideturtle()
            missilestate = "ready"
            missile.setposition(0, -400)
            # Reset the invader
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)
            invaderspeed += 0.5
            # Update the score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 18, 'normal'))

        # Check for a collision between the ship and invader
        if isCollision_invader_player(ship, invader):
            game_is_on = True
        if game_is_on is True:
            ship.hideturtle()
            missile.hideturtle()
            for i in invaders:
                i.hideturtle()
            screen.bgpic('./Images/Background(1).gif')
            break
    # Move the Missile
    if missilestate == 'fire':
        y = missile.ycor()
        y += missilespeed
        missile.sety(y)

    # Check if the missile has gone to the top
    if missile.ycor() > 275:
        missile.hideturtle()
        missilestate = 'ready'

# Many thanks to the tutorial on https://copyassignment.com/space-invaders-game-using-python/
