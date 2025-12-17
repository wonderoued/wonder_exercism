"""Functions to help the locomotive engineer."""


def get_list_of_wagons(locomotive_id, *wagons):
    """Return a list containing all wagon IDs, starting with the locomotive ID.

    :param locomotive_id: int - ID of the locomotive.
    :param wagons: tuple - collection of none, one or more wagon IDs.
    :return: list - list of all wagons.
    """

    return [locomotive_id, *wagons]


def fix_list_of_wagons(wagons, missing_wagons):
    """Reorder a list of wagon IDs according to a specific pattern.

    :param wagons: list - current list of wagon IDs.
    :param missing_wagons: list - wagons that need to be inserted.
    :return: list - the reordered list of wagon IDs.
    """

    # Selon l'exercice : les 2 premiers vont à la fin, le 3ème est la locomotive.
    w1, w2, loco, *rest = wagons
    return [loco, *missing_wagons, *rest, w1, w2]


def add_missing_stops(route, **stops):
    """Add missing stops to an existing route dict.

    :param route: dict - the current route dictionary.
    :param stops: dict - new stops to add to the route.
    :return: dict - updated route dictionary.
    """

    # On crée une nouvelle clé "stops" avec les valeurs fournies sans modifier les autres clés
    return {**route, "stops": list(stops.values())}


def extend_route_information(route_info, more_route_info):
    """Extend route information with more data.

    :param route_info: dict - route information and stops.
    :param more_route_info: dict - newer route information and stops.
    :return: dict - updated route information.
    """

    return {**route_info, **more_route_info}


def fix_wagon_depot(depot_rows):
    """Transpose the wagon depot data.

    :param depot_rows: list - nested list of wagons.
    :return: list - transposed list of wagons.
    """

    # Transposition de la matrice (lignes en colonnes)
    return [list(row) for row in zip(*depot_rows)]
