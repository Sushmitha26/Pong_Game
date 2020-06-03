#turtle module is used to do some basic graphics,for games,Using Turtle, we can easily draw in a drawing board.
import turtle
import winsound
wn=turtle.Screen()
wn.title("Pong by Sushmitha")
wn.bgcolor("black")
wn.setup(width=800, height=600)  
#tracer stops window from updating so we have to manually update it,it basically speeds up game
wn.tracer(0)


#Paddle A
paddle_a=turtle.Turtle()  #creates and retruns a new turtle object
paddle_a.speed(0)  #speed of animation,sets the speed to maximum,3-for slow
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()  #,picks the turtle pen, draw a line when moving.
paddle_a.goto(-350,0) #set positions x,y y=0 => vertically centered


#Paddle B
paddle_b=turtle.Turtle()  #creates and retruns a new turtle object
paddle_b.speed(0)  #speed of animation,not movement speed,sets the speed to maximum,3-for slow
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #20px wide,100px tall
paddle_b.penup()  #,picks the turtle pen, will not draw a line when moving.
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()  #creates and retruns a new turtle object
ball.speed(0)  #speed of animation,sets the speed to maximum,3-for slow
ball.shape('square')
ball.color('white')
ball.penup()  #,picks the turtle pen, draw a line when moving.
ball.goto(0,0)
#movement of ball
ball.dx = 0.2 #every time the ball moves by 0.1px right(coz positive)
ball.dy = 0.2  #0.1px up

#score
score_a = 0
score_b = 0


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #we just want to see text,not pen
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0",align="center", font=("Courier",24,"normal"))


#Function up 'a'
def paddle_a_up():
    y=paddle_a.ycor()  #ycor is from turtle module,returns the y-coordinate
    y += 20
    paddle_a.sety(y)  #sets y to the new y

#Function down 'a'
def paddle_a_down():
    y=paddle_a.ycor()  #ycor is from turtle module,returns the y-coordinate
    y -= 20
    paddle_a.sety(y)

#Function up 'b'
def paddle_b_up():
    y=paddle_b.ycor()  #ycor is from turtle module,returns the y-coordinate
    y += 20
    paddle_b.sety(y)  #sets y to the new y

#Function down 'b'
def paddle_b_down():
    y=paddle_b.ycor()  #ycor is from turtle module,returns the y-coordinate
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()   #tells to listen for keyboard input
wn.onkeypress(paddle_a_up, 'w')  #when u press lowercase w,calls the function
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'Up')  #when u press lowercase w,calls the function
wn.onkeypress(paddle_b_down, 'Down')


#Main game loop
while True:
    #every time the loop runs,it updates the screen
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    #height is 600,so +300 is y-coordinate at the top,and -300 at the bottom,and ball size is 20*20,so half is 10,300-10=290
    if(ball.ycor() > 290): #top
        ball.sety(290)
        ball.dy *= -1  #reverses the direction i.e. 0.1*-1 = -0.1
        #winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    elif(ball.ycor() < -290): #bottom
        ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    
    if(ball.xcor() > 350): #right
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #Delete turtle's drawings from the screen.State and position of turtle as well as drawings of other turtles are not affected.
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))


    elif(ball.xcor() < -350): #left
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))

    #paddle and ball collisions
    #ycor -> top of paddle and bottom of paddle
    if(ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    elif(ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        #for linux, os.system("aplay bounce.wav&")
        #for mac, os.system("afplay bounce.wav&")
        #winsound.PlaySound("pong.wav", winsound.SND_ASYNC)  #PlaySound is a wrapper around the Windows PlaySound API, SND_ASYNC ,similar to &, if the file is not async, program will stop,else it will play the sound in bg.
    
