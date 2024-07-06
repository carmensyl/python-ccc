import turtle
import winsound

# set window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#0002AB")
wn.setup(width=800, height=600)
# wn.tracer(0)

# Score tracking
score_l = 0
score_r = 0

# Left Paddle
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# Right Paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball movement
ball.dx = 3
ball.dy = -3

# Pen - Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Left: 0  |  Right: 0", align="center", font=("Courier", 24, "normal"))

# Functions moving left paddle up & down
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

# Functions moving right paddle up & down
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Keyboard binding to move paddles up & down
wn.listen()
wn.onkeypress(paddle_l_up,"w")
wn.onkeypress(paddle_l_down,"s")
wn.onkeypress(paddle_r_up,"Up")
wn.onkeypress(paddle_r_down,"Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #right + score to player left
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Left: {}  |  Right: {}".format(score_l, score_r), align="center", font=("Courier", 24, "normal"))
    # left + score to player right
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        pen.clear()
        pen.write("Left: {}  |  Right: {}".format(score_l, score_r), align="center", font=("Courier", 24, "normal"))

    # Paddle-ball collisions
    if 335 < ball.xcor() < 345 and (paddle_r.ycor()-50) < ball.ycor() < (paddle_r.ycor()+50):
        winsound.PlaySound("/bounce.wav", winsound.SND_ASYNC)
        delay = input
        ball.dx *= -1
    if -345 < ball.xcor() < -335 and (paddle_l.ycor()-50) < ball.ycor() < (paddle_l.ycor()+50):
        winsound.PlaySound("/bounce.wav", winsound.SND_ASYNC)
        delay = input
        ball.dx *= -1