def square_root(number):
    i = 1
    while i * i <= number:
        if i * i == number:
            return i
        i += 1
