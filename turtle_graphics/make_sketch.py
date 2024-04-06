from turtle import Turtle, Screen

jfk = Turtle()
scene = Screen()

#base functions
def move_forwards():
    jfk.fd(10)

def move_backwards():
    jfk.bk(10)

def turn_right():
    jfk.right(10)

def turn_left():
    jfk.left(10)

def clear():
    jfk.clear()
    jfk.up()
    jfk.home()
    jfk.down()
    
    


#event listener
scene.listen()
scene.onkey(key="w", fun=move_forwards)
scene.onkey(key="s", fun=move_backwards)
scene.onkey(key="d", fun=turn_right)
scene.onkey(key="a", fun=turn_left)
scene.onkey(key="c", fun=clear)
scene.exitonclick()