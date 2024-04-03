import colorgram

def extract_colors(image, num_colors):
    """
    extracts specified number of colors from an image in rgb format
    output: list of rgb tuples
    """
    colors = colorgram.extract(image, num_colors)
    color_tuples = []
    for color in colors:
        rgb = color.rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        color_tuples.append((red, green, blue))
    
    return color_tuples

hirst_colors = extract_colors('image.jpg', 15)

print(hirst_colors)