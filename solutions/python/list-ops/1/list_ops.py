def append(list1, list2):
    """Ajoute les éléments de la liste2 à la liste1."""
    new_liste = list1[:]
    for item in list2:
        new_liste += [item]
    return new_liste


def concat(lists):
    """Combine tous les éléments de toutes les listes en une seule liste applatie."""
    new_liste = []
    for sublist in lists:
        for item in sublist:
            new_liste += [item]
    return new_liste


def filter(function, lists):
    """renvoie la liste de tous les éléments pour lesquels predicate(item) est vrai) ."""
    filter_liste = []
    for item in lists:
        if function(item):
            filter_liste += [item]
    return filter_liste


def length(lists):
    """renvoie le nombre total d'éléments qu'elle contient) ."""
    count = 0
    for item in lists:
        count += 1
    return count


def map(function, lists):
    """renvoie la liste des résultats de l'application function(item) sur tous les éléments)."""
    result = []
    for item in lists:
        result += [function(item)]
    return result


def foldl(function, lists, initial):
    """replie (réduit) chaque élément dans l'accumulateur à partir de la gauche) ."""
    acc = initial
    for item in lists:
        acc = function(acc, item)
    return acc


def foldr(function, lists, initial):
    """replie (réduit) chaque élément dans l'accumulateur à partir de la droite)."""
    acc = initial
    for item in reverse(lists):
        acc = function(acc, item)
    return acc


def reverse(lists):
    """renvoie une liste contenant tous les éléments d'origine, mais dans l'ordre inverse)."""
    reversed_liste = []
    for item in lists:
        reversed_liste = [item] + reversed_liste
    return reversed_liste
