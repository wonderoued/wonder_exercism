def is_valid_triangle(sides):
    # D'abord, trier pour simplifier la vérification de l'inégalité
    a, b, c = sorted(sides)

    # 1. Tous les côtés doivent être > 0 (vérifier 'a' suffit si les côtés sont triés)
    if a <= 0:
        return False

    # 2. Inégalité triangulaire : La somme des deux plus petits (a, b)
    # doit être supérieure ou égale au plus grand (c).
    if a + b < c:
        return False

    return True


def equilateral(sides):
    """Détermine si un triangle est équilatéral."""
    # S'il n'est pas valide, ou si un côté est nul (comme [0,0,0]), c'est False.
    if not is_valid_triangle(sides):
        return False

    # Équilatéral : 1 seule longueur unique (les 3 côtés sont égaux)
    return len(set(sides)) == 1


def isosceles(sides):
    """Détermine si un triangle est isocèle."""
    # S'il n'est pas valide, c'est False.
    if not is_valid_triangle(sides):
        return False

    # Isocèle : 1 ou 2 longueurs uniques (au moins deux côtés sont égaux)
    return len(set(sides)) <= 2


def scalene(sides):
    """Détermine si un triangle est scalène."""
    # S'il n'est pas valide, c'est False.
    if not is_valid_triangle(sides):
        return False

    # Scalène : 3 longueurs uniques (tous les côtés sont différents)
    return len(set(sides)) == 3
