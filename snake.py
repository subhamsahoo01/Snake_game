import turtle as t




class Snake:
    def __init__(self):
        self.timmies=[]
        self.j = 0
        self.create_snake()
    def create_snake(self):
        for i in range(0,3):
            timmy=t.Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.setposition(self.j, 0)
            self.j -= 20
            self.timmies.append(timmy)


    # def move_snake(self):
    #     for i in range(1,len(self.timmies)+1):
    #         x_coordinate=self.timmies[len(self.timmies)-i-1].xcor()
    #         y_coordinate = self.timmies[len(self.timmies) - i - 1].ycor()
    #         self.timmies[len(self.timmies)-i].goto(x_coordinate,y_coordinate)
    #     self.timmies[0].forward(20)
    def move_snake(self):
        # Move the snake's body from tail to head
        for i in range(len(self.timmies) - 1, 0, -1):  # Start from the second-to-last segment
            x_coordinate = self.timmies[i - 1].xcor()  # Get the position of the previous segment
            y_coordinate = self.timmies[i - 1].ycor()  # Get the position of the previous segment
            self.timmies[i].goto(x_coordinate, y_coordinate)  # Move the current segment to that position

        # Move the head forward
        self.timmies[0].forward(20)  # The first segment (head) moves forward by 20 pixels
    def up(self):
        if self.timmies[0].heading() !=270:
            self.timmies[0].setheading(90)

    def down(self):
        if self.timmies[0].heading() !=90:
            self.timmies[0].setheading(270)

    def right(self):
        if self.timmies[0].heading() !=180:
            self.timmies[0].setheading(0)

    def left(self):
        if self.timmies[0].heading() !=0:
            self.timmies[0].setheading(180)


    def extend_snake(self):
        tim=t.Turtle(shape="square")

        tim.color("white")
        tim.penup()
        tim.goto(self.timmies[-1].position())

        self.timmies.append(tim)


