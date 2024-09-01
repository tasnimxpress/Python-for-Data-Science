import colorgram as cg

image = cg.extract('Day-18/spot_paint/hirst_spot_paint.png', 7)

color_list = []
for color in image:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)

    color_list.append(rgb)

# print(color_list)
