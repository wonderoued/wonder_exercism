COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    first_color = colors[0]
    second_color = colors[1]
    tens = COLORS.index(first_color)
    units = COLORS.index(second_color)
    return tens * 10 + units
