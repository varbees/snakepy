from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("darkgrey")
    self.speed('fastest')
    self.shapesize(stretch_wid = 0.6, stretch_len = 0.6)
    self.refresh()


# Experimental code for Bonus food
  # def foodsize(self, score):
  #   if score % 5 != 0:
  #     self.color('purple')
  #     self.refresh()
  #   elif score >=5 and score % 5==0:
  #     self.color("red")
  #     self.shapesize(stretch_wid = 1, stretch_len = 1)
  #     self.refresh()

  def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)
