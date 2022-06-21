import turtle
import time

window = turtle.Screen()
window.title("PONG YEA BOI!")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Keep Score
score_one = 0
score_two = 0

#Paddle One
paddle_one = turtle.Turtle()
paddle_one.speed(0) #set to max speed
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_one.penup()
paddle_one.goto(-350,0)


#Paddle Two
paddle_two = turtle.Turtle()
paddle_two.speed(0) #set to max speed
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_two.penup()
paddle_two.goto(350,0)

#ball
b = turtle.Turtle()
b.speed(0) #set to max speed
b.shape("circle")
b.color("purple")
b.penup()
b.goto(0,0)

b.dx = 0.1
b.dy = -0.1

#create pen object
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color("white")
pencil.penup()
pencil.hideturtle()
pencil.goto(0,270)
pencil.write("Player 1: 0         Player 2: 0", align = "center", font= ("Arial",20,"normal"))

def paddle_one_up():
    y = paddle_one.ycor()
    y= y + 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y= y - 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y= y + 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y= y - 20
    paddle_two.sety(y)

#keyboard binding
window.listen() #listen to keyboard
window.onkeypress(paddle_one_up,'w')
window.onkeypress(paddle_one_down,'s')
window.onkeypress(paddle_two_up,'Up')
window.onkeypress(paddle_two_down,'Down')

while True:
    window.update()

    #Move ball
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)

    #At border
    if b.ycor()>290:
        b.sety(290)
        b.dy *= -1

    if b.ycor()<-290:
        b.sety(-290)
        b.dy *= -1

    if b.xcor() > 390:
        b.goto(0,0)
        b.dx *= -1
        score_one = score_one + 1
        pencil.clear()
        pencil.write("Player 1: {}         Player 2: {}".format(score_one,score_two), align = "center", font= ("Arial",20,"normal"))
        time.sleep(3)


    if b.xcor() < -390:
        b.goto(0,0)
        b.dx *= -1
        score_two = score_two + 1
        pencil.clear()
        pencil.write("Player 1: {}         Player 2: {}".format(score_one,score_two), align = "center", font= ("Arial",20,"normal"))
        time.sleep(3)
        
    #paddle collision
    if (b.xcor() > 340 and b.xcor()<350) and (b.ycor() < paddle_two.ycor() + 40 and b.ycor() > paddle_two.ycor()- 40):
        b.setx(340)
        b.dx *= -1

    if (b.xcor() < -340 and b.xcor()>-350) and (b.ycor() < paddle_one.ycor() + 40 and b.ycor() > paddle_one.ycor()- 40):
        b.setx(-340)
        b.dx *= -1

    if score_one == 15:
        pencil.goto(0,0)
        pencil.write("Player 1 Wins!", align = "center", font= ("Arial",20,"normal"))
        time.sleep(10)
        break

    if score_two == 15:
        pencil.goto(0,0)
        pencil.write("Player 2 Wins!", align = "center", font= ("Arial",20,"normal"))
        time.sleep(10)
        break
        
            
