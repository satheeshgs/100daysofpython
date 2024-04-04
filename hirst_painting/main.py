import colorgram, random
from turtle import Turtle, Screen

def extract_colors(image, num_colors):
    """
    extracts specified number of colors from an image in rgb format
    output: list of rgb tuples
    """
    colors = colorgram.extract(image, num_colors)
    color_tuples = []
    for color in colors:
        rgb = color.rgb
        red = rgb.r
        green = rgb.g
        blue = rgb.b
        color_tuples.append((red, green, blue))
    
    return color_tuples

hirst_colors = extract_colors('image.jpg', 15)

jfk = Turtle()
scene = Screen()
scene.colormode(255)
jfk.up()
jfk.setpos(-200,-200)
jfk.dot(20, random.choice(hirst_colors))



#painting start
for i in range(10):
    for j in range(10):
        jfk.dot(20, random.choice(hirst_colors))
        jfk.fd(50)
    jfk.setpos(-200, jfk.ycor()+50)

jfk.home()   

scene.exitonclick()