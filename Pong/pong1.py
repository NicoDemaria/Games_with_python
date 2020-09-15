import turtle

wn = turtle.Screen()
wn.title('Pongo por el mike')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,y=0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,y=0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,y=0)
ball.dx = .1
ball.dy = .1


# Function
# A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Ball Function


# Keyboard binding
wn.listen()

# Pad derecho
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
# Pad izquierdo
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')















# Main game loop
while True:
    wn.update()





    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)




    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1








