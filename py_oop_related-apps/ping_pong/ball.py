from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        # we can slow the ball movements by replacing 10 with 0.1
        # another alternative is to import time module, and use time.sleep() method
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # we reverse the y_move coordinate, which then is decreasing
        # the x_move coordinate remains constant, increases

    def bounce_x(self):  # this class means the ball touches the paddle
        self.x_move *= -1  # we reverse the x_move coordinate, which then is decreasing
        # the y_move coordinate remains constant, increases

        self.move_speed *= 0.95
        # this increases the ball speed a bit each time it touches a paddle
        # 0.08 x 0.95 = 0.076 , which increases the time.sleep()

    def reset_position(self):
        # resets the ball to its primary origin once a player loses
        self.goto(0, 0)
        # resets the ball speed once a player loses, to avoid the ball increasing in speed indefinitely
        self.move_speed = 0.08
        self.bounce_x()