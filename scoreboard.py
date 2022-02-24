from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("high_score.txt")
        high_score = int(file.read())
        self.high_score = high_score
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.display()


    def display(self):
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.high_score}", move=False,align=ALIGNMENT, font=FONT)


    def add_point(self):
        self.score += 1
        self.display()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score.txt", 'w')
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.display()