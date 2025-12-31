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


def label(colors):
    d1 = COLORS.index(colors[0])
    d2 = COLORS.index(colors[1])
    exp = COLORS.index(colors[2])
    value = (d1 * 10 + d2) * (10**exp)
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_index = 0
    while value >= 1000 and unit_index < len(units) - 1:
        value //= 1000
        unit_index += 1
    return f"{value} {units[unit_index]}"
