from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.life_number = 2
        self.score = 0
        self.display()

    def decrease_life(self):
        self.life_number -= 1
        self.display()

    def increase_score(self):
        self.score += 1
        self.display()

    def defeat(self):
        self.clear()
        self.goto(-90, 0)
        self.write("You Lose! Push 'R' to restart.", font=("Courior", 10, "normal"))

    def victory(self):
        self.clear()
        self.goto(-90, 0)
        self.write("You win! Push 'R' to restart.", font=("Courior", 10, "normal"))

    def display(self):
        self.clear()
        self.goto(-90, 280)
        self.write(f"Lives Remaining: {self.life_number}  Score: {self.score}", font=("Courior", 10, "normal"))


