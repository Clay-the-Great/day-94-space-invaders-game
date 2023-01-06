from turtle import Turtle


class EnemyBullet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.2)
        self.speed("fastest")
        self.color("red")

    def move(self):
        self.setheading(270)
        self.forward(20)