import turtle
import time
import random
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

delay = 0.1
score = 0
high_score = 0

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


segments = []


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(lambda: head.sety(head.ycor() + 20), "Up")
wn.onkeypress(lambda: head.sety(head.ycor() - 20), "Down")
wn.onkeypress(lambda: head.setx(head.xcor() - 20), "Left")
wn.onkeypress(lambda: head.setx(head.xcor() + 20), "Right")


while True:
    wn.update()

    
    move()

   
    if head.distance(food) < 20:
        
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        
        score += 10
        if score > high_score:
            high_score = score

    
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    time.sleep(delay)
wn.bye()
