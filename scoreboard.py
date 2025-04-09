import turtle

class Score_Board(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.i=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.write(f"Score ={self.i}",False,align="center",font=('Arial',14,'normal'))


    def refresh_scoreboard(self):
        self.i+=1
        self.clear()
        self.goto(0,280)
        self.write(f"Score ={self.i}", False, align="center", font=('Arial', 14, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 14, 'normal'))