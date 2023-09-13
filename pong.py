import turtle

wn=turtle.Screen()
wn.title("pong")
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.cv._rootwindow.resizable(False, False)

#left paddle
paddle_left=turtle.Turtle()
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.speed(0)
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)


#right paddle
paddle_right=turtle.Turtle()
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.speed(0)
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)


#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=0.20
ball.dy=0.20

#score
player_A=0
player_B=0



pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("player A:{}     player B:{}".format(player_A,player_B),align="center",font=("courier",24))




#moving paddles

def paddle_left_up():
    if paddle_left.ycor()+40 < 300:
        y=paddle_left.ycor()
        y+=20
        paddle_left.sety(y)

def paddle_left_down():
    if paddle_left.ycor() >-240:
        y=paddle_left.ycor()
        y-=20
        paddle_left.sety(y)

def paddle_right_up():
    if paddle_right.ycor() +40 < 300:
        y=paddle_right.ycor()
        y+=20
        paddle_right.sety(y)

def paddle_right_down():
    if paddle_right.ycor() >-240:
        y=paddle_right.ycor()
        y-=20
        paddle_right.sety(y)

#keyboard

wn.listen()
wn.onkeypress(paddle_left_up,'w')
wn.onkeypress(paddle_left_down,'s')
wn.onkeypress(paddle_right_up,'Up')
wn.onkeypress(paddle_right_down,'Down')

#game loop

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    elif ball.xcor()>390:
        player_A+=1
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        pen.write("player A:{}     player B:{}".format(player_A,player_B),align="center",font=("courier",24))


    elif ball.xcor()<-390:
        ball.goto(0,0)
        player_B+=1
        ball.dx*=-1
        pen.clear()
        pen.write("player A:{}     player B:{}".format(player_A,player_B),align="center",font=("courier",24))


    #paddle and bounce

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor()- 40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor()- 40):
        ball.setx(-340)
        ball.dx*=-1

    

