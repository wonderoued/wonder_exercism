def factors(value):
    prime_liste = []

    while value % 2 == 0:
        prime_liste.append(2)
        value //= 2


    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            prime_liste.append(divisor)
            value //= divisor
        else:
            divisor += 2


    if value > 1:
        prime_liste.append(value)


    return prime_liste

n = factors(60)
print(f"Les facteurs premiers du nombre 60 sont : {n}")
