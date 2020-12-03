#uses when you know exactly how many times do something
import turtle
jobzz_turtle=turtle.Turtle()
jobzz_turtle.speed(15) #to set the speed of the turtle
 

def triangle():
  jobzz_turtle.forward(140)
  jobzz_turtle.left(150)
  jobzz_turtle.forward(80)
  jobzz_turtle.left(60)
  jobzz_turtle.forward(80)
  
for i in range(3):
  triangle(3)  #draw triangle for three times
