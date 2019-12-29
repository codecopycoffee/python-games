import turtle

wndw = turtle.Screen()
wndw.title("")
wndw.title("Pong Game")
wndw.bgcolor("purple")
wndw.setup(width=800, height=600)
wndw.tracer(0)

#Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("orange")
paddle_r.penup()
paddle_r.goto(350, 0)
paddle_r.shapesize(stretch_wid=5, stretch_len=1)

#Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("green")
paddle_l.penup()
paddle_l.goto(-350, 0)
paddle_l.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#Paddle Motion
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y += -20
    paddle_r.sety(y)

def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y += -20
    paddle_l.sety(y)

wndw.listen()
wndw.onkey(paddle_r_up, "i")
wndw.onkey(paddle_r_down, "k")
wndw.onkey(paddle_l_up, "w")
wndw.onkey(paddle_l_down, "s")

#Main game loop
while True:
    wndw.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Ball Movement
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    #Ball and Paddle Interaction
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
