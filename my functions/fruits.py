fruit_to_color = {
    'banana': 'yellow',
    'cherry': 'red',
    'orange': 'orange',
    'pear': 'green',
    'peach': 'orange',
    'plum': 'purple',
    'pomegranate': 'red',
    'strawberry': 'red'}

# Invert fruit_to_color
color_to_fruit = {}
for fruit in fruit_to_color:
    # extract the color corresponding to that fruit.
    color = fruit_to_color[fruit]
    '''# add the new color to fruit dictionary the color to fruit entry.
    color_to_fruit[color] = fruit'''

    # If color is not already a key in the accumulator,
    #add a color:[fruit] as an entry.
    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]
    # Otherwise, append fruit to that existing list. 
    else:
        color_to_fruit[color].append(fruit)   
