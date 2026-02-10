def square_of_sum(number):
    """calcule du carré de la somme de N en appliquant la formule de Gauss."""
    sum_n = (number * (number + 1)) // 2
    square_sum = sum_n ** 2
    return square_sum

def sum_of_squares(number):
    """calcul la somme des carré."""
    sum_square = (number * (number + 1) * (2 * number + 1)) // 6
    return sum_square


def difference_of_squares(number):
    "calcul la différence entre le carré des sommes d'un nombre N et la somme des carré."
    square_sum = square_of_sum(number)
    sum_square = sum_of_squares(number)
    return square_sum - sum_square
