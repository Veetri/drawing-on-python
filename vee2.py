import turtle

#initialize methot
bat = turtle.Turtle()

#size of pointer and pen
bat.turtlesize(1, 1, 1)
bat.pensize(3)

#screen info
wn = turtle.Screen()
wn.bgcolor("dark red")
wn.title("VEE3")

#color
bat.color("white", "black")

#begin filling color
bat.begin_fill()

#trun1
bat.left(90)
bat.circle(50, 85)
bat.circle(15, 110)
bat.right(180)

#trun2
bat.circle(30, 150)
bat.right(5)
bat.forward(10)

#trun3
bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

#trun4
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

#trun5
bat.forward(30)
bat.left(55)
bat.forward(10)

#reverse

#trun5
bat.forward(10)
bat.left(55)
bat.forward(30)

#trun4
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

#trun3
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

#trun2
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

#trun1
bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

#end color filling
bat.end_fill()

#end the turtle method
turtle.done()





