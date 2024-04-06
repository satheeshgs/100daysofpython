from turtle import Turtle, Screen

jfk = Turtle()
scene = Screen()

def move_forwards():
    jfk.fd(10)

#event listener
scene.listen()
scene.onkey(key="space", fun=move_forwards)
scene.exitonclick()