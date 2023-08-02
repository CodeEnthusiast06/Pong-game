import turtle


#window
wn = turtle.Screen()
wn.title("Pong by ashish")
wn.bgcolor("black")
wn.setup(width=600, height=400)
wn.tracer(0)

#score 
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.speed(0)
paddle_a.goto(-250,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.speed(0)
paddle_b.goto(250,0)

#ball
ball= turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.hideturtle()
pen.goto(0,160)
pen.write(f"Player A:{score_a}  Player B:{score_b}",align = "center",font=("Courier",15,"normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"g")
wn.onkeypress(paddle_a_down,"h")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main game loop

while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border check
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy*=-1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy*=-1

    if ball.xcor() > 250:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write(f"Player A:{score_a}  Player B:{score_b}",align = "center",font=("Courier",15,"normal"))    
            
    if ball.xcor() < -250:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write(f"Player A:{score_a}  Player B:{score_b}",align = "center",font=("Courier",15,"normal"))

    #Paddle ball collisions
    if ball.xcor() > 230 and ball.xcor() < 250 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50:
        ball.dx*=-1   
    if ball.xcor() < -230 and ball.xcor() > -250 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50:
        ball.dx*=-1 
