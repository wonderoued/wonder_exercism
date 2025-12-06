def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Alternatively, you can use the 'and' and 'or' logical operators for the comparison.
# return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
