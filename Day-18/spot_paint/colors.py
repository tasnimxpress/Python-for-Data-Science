import colorgram as cg

image = cg.extract('Day-18/hirst_spot_paint.png', 7)

color_list = []
for i in range(len(image)):
    color = image[i]
    rgb_color = color.rgb
    r = rgb_color.r
    g = rgb_color.g
    b = rgb_color.b
    rgb = (r, g, b)

    color_list.append(rgb)

print(color_list)
