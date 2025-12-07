def square(number):
    """calculate the grain's number on a given square of (1 to 64)
    :param: number: int - the square's number (1 to 64).
    :return: int - the grain's number on the square .
    """
    # verification of limites and to raise exception ValueError.
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    # the formule is 2 ** number.
    return 2 ** (number - 1)

    # alternatively with the binary operator <<.
    # return 2 << (number - 1)


def total():
    """calculate the total numbre of grain on the chessboard (64 squares)
    :return: int - the total number of grain.
    """
    # the total is 2 ** 64
    return (2**64) - 1

    # alternatively with the binary operator.
    # return (2 << 64) - 1
