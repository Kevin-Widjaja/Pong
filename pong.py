import turtle  # basic module for game development

# Control Window Display
wn = turtle.Screen()  # create window object
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600) # dimensions are in px, top of window is +300, bottom is -300
wn.tracer(0) # prevents the window from updating, requires manual updates, speeds up the game

def play():
    wn.clearscreen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.tracer(0) # prevents the window from updating, requires manual updates, speeds up the game

    # Paddle A
    paddle_a = turtle.Turtle() # this is going to be a turtle object (`turtle` is the module name, `Turtle` is the class name)
    paddle_a.speed(0) # sets paddle speed animation to max
    paddle_a.shape("square") 
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1) # this stretches the width/height by 5x, so 100px tall, 20px in length
    paddle_a.penup() # default for turtle is to have a pen down to draw lines
    paddle_a.goto(-350, 0) # starting position is -350 in the x-axis, 0 in the y-axis

    # Paddle B
    paddle_b = turtle.Turtle() 
    paddle_b.speed(0) 
    paddle_b.shape("square") 
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
    paddle_b.penup() 
    paddle_b.goto(350, 0) 

    # Ball
    ball = turtle.Turtle()
    ball.shape("circle") 
    ball.speed(0) 
    ball.color("white")
    ball.penup() 
    ball.goto(0, 0)
    ball.dx = 3 # controls movement of ball, every time it moves, moves by 2px to left/right
    ball.dy = 3

    # Scoreboard
    score_a = 0
    score_b = 0
    scoreboard = turtle.Turtle()
    scoreboard.speed(0)
    scoreboard.color("white")
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0, 260) # make the scoreboard top of the screen
    scoreboard.write("Player 1: {} | Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Functions for movement
    def paddle_a_up():
        y = paddle_a.ycor() # returns the y-coordinate of the paddle_a object
        y += 20 # adds 20px to the y-coordinate
        paddle_a.sety(y) # sets the new y-coordinate

    def paddle_a_down():
        y = paddle_a.ycor() 
        y -= 20 # subtracts 20px to the y-coordinate
        paddle_a.sety(y) 

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Waiting for keyboard click to move
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    # Main game loop
    while True:
        wn.update() # every time loops runs, update screen

        # start by moving the ball
        ball.setx(ball.xcor() + ball.dx) # we will set the x-coordinate of the ball to move 
        ball.sety(ball.ycor() + ball.dy)

        # check to see if the ball hits either the top or bottome border, reverse ball direction
        if ball.ycor() > 290 or ball.ycor() < -290: # since top of screen is +300, and ball height is 20px
            ball.dy *= -1 # changes direction of the ball

        # check to see if either person has scored and then move ball back to center, reverse ball direction, and update scoreboard
        if ball.xcor() > 390: 
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            scoreboard.clear()
            scoreboard.write("Player 1: {} | Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            scoreboard.clear()
            scoreboard.write("Player 1: {} | Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # if ball hits the paddle, it will bounce off
        if ( 
            ball.xcor() < -340 and ball.xcor() > -350
            and ball.ycor() < paddle_a.ycor() + 40
            and ball.ycor() > paddle_a.ycor() - 40
        ):
            ball.setx(-340)
            ball.dx *= -1

        if ( # if ball hits paddle b
            ball.xcor() > 340 and ball.xcor() < 350
            and ball.ycor() < paddle_b.ycor() + 40
            and ball.ycor() > paddle_b.ycor() - 40
        ):
            ball.setx(340)
            ball.dx *= -1

        # paddles can't go past the borders
        if paddle_a.ycor() >= 260:
            paddle_a_down()
        if paddle_a.ycor() <= -260:
            paddle_a_up()
        if paddle_b.ycor() >= 260:
            paddle_b_down()
        if paddle_b.ycor() <= -260:
            paddle_b_up()

        if score_a >= 3 or score_b >= 3:
            winningMessage = turtle.Turtle()
            winningMessage.speed(0)
            winningMessage.color("white")
            winningMessage.penup()
            winningMessage.hideturtle()
            winningMessage.goto(0, 150) # make the scoreboard top of the screen
            
            if score_a > score_b:
                winningMessage.write("Congratulations player 1, you've won!", align="center", font = ("Courier", 30, "normal"))
            
            else: 
                winningMessage.write("Congratulations player 2, you've won!", align="center", font = ("Courier", 30, "normal"))

            break


def mainMenu():
    startMessage = turtle.Turtle()
    startMessage.speed(0)
    startMessage.color("white")
    startMessage.shape("blank")
    startMessage.penup()
    startMessage.setposition(0,75)
    startMessage.pendown()
    startMessage.write("Press space to start a new game", align="center", font = ("Courier", 36, "bold"))

    rules = turtle.Turtle()
    rules.speed(0)
    rules.color("white")
    rules.shape("blank")
    rules.penup()

    rules.setposition(0,25)
    rules.write("Player 1: 'W' and 'S' to move", align="center", font = ("Courier", 24, "bold"))

    rules.setposition(0,0)
    rules.write("Player 2: 'UP' and 'DOWN' to move", align="center", font = ("Courier", 24, "bold"))

    rules.setposition(0,-25)
    rules.write("First to 3 wins", align="center", font = ("Courier", 24, "bold"))

while True:
    wn.listen()
    mainMenu()
    wn.onkeypress(play, "space")