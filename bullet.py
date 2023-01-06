from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.2)
        self.speed("fastest")
        self.color("white")
        self.visible = True

    def move(self):
        self.setheading(90)
        self.forward(20)

    def disappear(self):
        self.hideturtle()
        self.visible = False
