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

TOLERANCES = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def resistor_label(colors):
    if len(colors) == 1:
        return f"{COLORS.index(colors[0])} ohms"

    tolerance_color = colors[-1]
    multiplier_color = colors[-2]
    digit_color = colors[:-2]
    value = 0
    for color in digit_color:
        value = value * 10 + COLORS.index(color)

    value *= 10 ** COLORS.index(multiplier_color)

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_index = 0
    temp_value = float(value)
    while temp_value >= 1000 and unit_index < len(units) - 1:
        temp_value /= 1000
        unit_index += 1

    if temp_value == int(temp_value):
        formatted_value = int(temp_value)
    else:
        formatted_value = temp_value

    tolerance = TOLERANCES[tolerance_color]
    return f"{formatted_value} {units[unit_index]} {tolerance}"
