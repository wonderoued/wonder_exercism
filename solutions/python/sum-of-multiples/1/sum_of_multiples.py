def sum_of_multiples(limit, multiples):
    multiple_sum = set()
    for m in multiples:
        if m == 0:
            continue
        for val in range(m, limit, m):
            multiple_sum.add(val)
            
    return sum(multiple_sum)