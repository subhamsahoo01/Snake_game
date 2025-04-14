import turtle

class Score_Board(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.i=0
        with open("data.txt",mode="r") as file:
            self.high_score=file.read()

        self.tim1=turtle.Turtle()
        self.tim2=turtle.Turtle()
        self.tim3=turtle.Turtle()
        self.tim3.color("white")
        self.tim3.hideturtle()
        self.tim3.penup()
        self.tim1.color("white")
        self.tim1.hideturtle()
        self.tim1.penup()
        self.tim1.goto(0,280)
        self.tim1.write(f"Score ={self.i}",False,align="center",font=('Arial',14,'normal'))
        self.tim2.color("white")
        self.tim2.hideturtle()
        self.tim2.penup()
        self.tim2.goto(100, 280)
        self.tim2.write(f"Highest Score={self.high_score}", False, align="center", font=('Arial', 14, 'normal'))


    def refresh_scoreboard(self):
        self.i+=1
        self.tim1.clear()
        self.tim1.goto(0,280)
        self.tim1.write(f"Score ={self.i}", False, align="center", font=('Arial', 14, 'normal'))
    def game_over(self):
        self.tim3.goto(0,0)
        self.tim3.write(f"GAME OVER", False, align="center", font=('Arial', 14, 'normal'))
    def refresh_highscore(self):
        with open("data.txt", mode="r") as file:
            content = file.read()
        if self.i>int(content):
            with open("data.txt",mode="w+") as file:
                file.write(f"{self.i}")
        with open("data.txt",mode="r") as file:
            contents=file.read()

        self.tim2.clear()
        self.tim2.goto(100,280)
        self.tim2.write(f"Highest Score={contents}",False,align="center",font=('Arial', 14, 'normal'))