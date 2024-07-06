# Objective
To create a mini pong game using python turtle module.

# Requirements
1. A ball starts in the middle of the screen, and move to right to start the game.
2. Two paddles, one on the left and one on the right, controlled by 2 players with separate keyboard keys to bounce back the ball to the other side.
3. A sound is played during each hit.
4. When the ball reaches left or right window border, score is added to player of the other side. Ball is reset to center.
5. When the ball reaches top or bottom window border, it bounces back along the y axis.
6. Score tracking and display.

# Project Timeline
|Day|Tasks|
|---|---|
|1|Set up screen, create ball and paddles, set ball initial movement and border check|
|2|Add functions to control the paddles and set up conditions for ball-paddle collision to bounce the ball back|
|3|Create score display and tracking, fine-tune color and ball speed, add sound effect to indicate ball-paddle collision|

# Methods
1. Use the turtle module in Python library to create a small window for the game. 
2. Use turtle to create circle and rectangle shapes representing ball and paddles.
3. Change the x and y coordinates of the shapes to make them move.
4. Use listen() to bind keyboard keys to functions moving paddles.
5. Apply if conditions regarding ball coordinates to change ball direction during border check and paddle collision.
6. Use pen.write() in turtle module to print the score display.
7. Use variables to store the scores, and if conditions to increase the scores when touching left or right window border.
8. Use pen.clear() and pen.write() to update the scores.
9. Add sound effect for ball-paddle collision with the winsound module.

# Code
```py
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
```

# Result
Left player scores when ball touches right window border and vice versa
![Left player scores when ball touches right window border and vice versa](pong01.jpg)

Players use keyboard to control up and down of paddles
![Players use keyboard to control up and down of paddles](pong02.jpg)

# Resources
[1. Learn Python by Building Five Games - Full Course](https://www.youtube.com/watch?v=XGf2GcyHPhc&t=78s&ab_channel=freeCodeCamp.org)

[2. How to Play a Sound in Windows with Python](https://www.youtube.com/watch?v=1FyqFqAN9UM&ab_channel=TokyoEdtech)

# What's next
1. Create more random paths at game start for the ball to add variety to the game.

2. Include a quick countdown before each game start to make it more exciting and let players rest a bit.

3. Increase the ball speed slightly to increase the difficulty gradually if players can keep hitting the ball.

4. End the game when the score of any one side is up to a certain number.
