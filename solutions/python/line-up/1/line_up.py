def line_up(name, number):
    two_number = number % 100
    last_number = number % 10
    if 11 <= two_number <= 13:
        suffix = "th"
    elif last_number == 1:
        suffix = "st"
    elif last_number == 2:
        suffix = "nd"
    elif last_number == 3:
        suffix = "rd"
    else:
        suffix = "th"

    sentence = f"{name.capitalize()}, you are the {number}{suffix} customer we serve today. Thank you!"
    return sentence
