import turtle
jobzz_turtle=turtle.Turtle()

def square():
  
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  jobzz_turtle.right(90)
  jobzz_turtle.forward(100)
  
#if elephant w8 is greater than ant's w8 draw a square
elephant_w8 = 3000
ant_w8 = 1
if elephant_w8 > ant_w8:
  square()

