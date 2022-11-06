from turtle import Turtle

# ---- Invader Pattern ---- #

y_cords = [350, 350, 350, 350, 350, 350, 350, 350,
           310, 310, 310, 310, 310, 310, 310, 310,
           270, 270, 270, 270, 270, 270, 270, 270,
           230, 230, 230, 230, 230, 230, 230, 230]

x_cords = [-280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280]


class Invaders:
    def __init__(self):
        self.all_invaders = []

    def create_invader(self):
        for invader_index in range(0, 32):
            new_invader = Turtle(shape='./images/invader.gif')
            new_invader.penup()
            new_invader.goto(x_cords[invader_index], y_cords[invader_index])
            self.all_invaders.append(new_invader)

