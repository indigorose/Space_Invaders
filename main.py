# ---- Main Imports ---- #
import turtle
from turtle import *
import math
import random
import time

# ---- Class Imports ---- #
from ship import Ship
from missile import Missile
from invader import Invaders
from scoreboard import Scoreboard


# ---- Screen Setup ---- #
screen = Screen()
screen.setup(width=700, height=800)
screen.bgcolor('black')
screen.title("Space Invaders")


# ---- Game Icons ---- #
turtle.register_shape('./images/invader.gif')
turtle.register_shape('./images/player.gif')

# ---- Invaders ---- #
invaders = Invaders()

# ---- Game Play ---- #

scoreboard = Scoreboard()
game_is_on = True
# while game_is_on:
#     time.sleep(0.01)
#     screen.update()
#     game_is_on = False

screen.exitonclick()
