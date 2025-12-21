"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the value  s as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if is_sublist(list_one, list_two):
        return SUBLIST

    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(small_list, big_list):
    if not small_list:
        return True
    len_s = len(small_list)
    len_b = len(big_list)
    for i in range(len_b - len_s + 1):
        if big_list[i : i + len_s] == small_list:
            return True
    return False
