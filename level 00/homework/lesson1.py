from turtle import *
#we want peint a house
#step 1:  draw a square
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
#drawing a door
forward(200)
left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,  200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
left(120)
forward(20)
color("brown")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
color("purple")
begin_fill()
right(90)
forward(60)
color("brown")
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()





























exitonclick()