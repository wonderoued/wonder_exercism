"""determine the score for a dart toss at a target"""


def score(x, y):
    """calculate the score of a dart landing at a coordinates (x, y).

    :param x: float - x coordinate of the dart,
    :param y: float - y coordinate of the dart,
    :return: int - the score earned.
    """
    squared_distance = x**2 + y**2
    if squared_distance <= 1:
        return 10
    if squared_distance <= 25:
        return 5
    if squared_distance <= 100:
        return 1
    return 0
