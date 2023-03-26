#Event Listners

#from turtle import Turtle, Screen
#ted=Turtle()
#screen=Screen()
#def move_fd():
#    ted.fd(10)
#screen.listen()
#screen.onkey(fun=move_fd,key="a")
#screen.exitonclick()

#Etch-A Sketch app

#from turtle import Turtle, Screen
#ted=Turtle()
#screen=Screen()
#def move_right():
#    ted.fd(10)
#def move_up():
#    ted.left(10)
#def move_down():
#    ted.right(10)
#def move_left():
#    ted.backward(10)
#def Clear():
#    ted.clear()
#    ted.pu()
#    ted.home()
#screen.listen()
#screen.onkey(fun=move_right,key="d")
#screen.onkey(fun=move_left,key="a")
#screen.onkey(fun=move_up,key="w")
#screen.onkey(fun=move_down,key="x")
#screen.onkey(fun=Clear,key="c")
#screen.exitonclick()


from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(500, 400)
colors=["red","blue","green","yellow","orange","purple"]
y_coordinates=[60,30,0,-30,-60,-90]
all_turtles=[]
is_race=False
user_bet=screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race=True
while is_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race=False
            winner_color=turtle.pencolor()
            if user_bet==winner_color:
                print(f"You've won and {winner_color} is the winning turtle.")
            else:
                print(f"You've lost and {winner_color} is the winning turtle.")
        random_distance=random.randint(0,10)
        turtle.fd(random_distance)
screen.exitonclick()
