from food import Food
from snake import Snake
from turtle import Screen, Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.write(f'Score: {self.score}', align='center', font=('Arial', 20, 'normal'))
    self.hideturtle()
    self.update_score()

  def update_score(self):
    self.write(f'Score: {self.score}', align='center', font=('Arial', 20, 'normal'))

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score()


  def game_over(self):
    self.goto(0,0)
    self.color('red')
    self.write('GAME OVER', align='center', font=('Arial', 22, 'normal'))
    self.goto(0,-30)
    self.color('white')
    self.write('\nPress SPACE to try Again', 
                align='center', 
                font=('Arial',22,'normal'))

