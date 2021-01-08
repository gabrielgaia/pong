from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.__move_speed = 0.1
        self.__x_key = 0
        self.random_x_key()
        self.__y_key = 0
        self.random_y_key()
        self.penup()
        self.shape('circle')
        self.color('white')

    @property
    def move_speed(self):
        return self.__move_speed

    def random_x_key(self):
        self.__x_key = 0
        while self.__x_key == 0:
            self.__x_key = randint(-50, 50)
            if self.__x_key < 0:
                self.__x_key = -1
            elif self.__x_key > 0:
                self.__x_key = 1

    def random_y_key(self):
        self.__y_key = 0
        while self.__y_key == 0:
            self.__y_key = randint(-50, 50)
            if self.__y_key < 0:
                self.__y_key = -1
            elif self.__y_key > 0:
                self.__y_key = 1

    def move(self):
        new_x = self.xcor() + (self.__x_key * 10)
        new_y = self.ycor() + (self.__y_key * 10)
        self.goto((new_x, new_y))

    def change_direction_wall(self):
        self.__y_key *= -1

    def change_direction_paddle(self):
        self.__move_speed *= 0.9
        self.__x_key *= -1

    def goal(self):
        self.__move_speed = 0.1
        self.home()
        self.random_y_key()
        self.__x_key *= -1
