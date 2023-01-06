from turtle import Turtle
import random


class Invader(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.speed("fastest")
        self.color("white")
        self.goto(x, y)
        self.visible = True

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def fire(self):
        number = random.randint(0, 50)
        if number == 0:
            return True
        else:
            return False

    def disappear(self):
        self.hideturtle()
        self.visible = False



