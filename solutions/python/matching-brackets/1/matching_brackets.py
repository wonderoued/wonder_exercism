def is_paired(input_string):
    pairs = {")": "(", "]": "[", "}": "{"}
    ouvrant = "([{"
    fermant = ")]}"
    pile = []
    for char in input_string:
        if char in ouvrant:
            pile.append(char)
        elif char in fermant:
            if not pile or pile.pop() != pairs[char]:
                return False
    return len(pile) == 0
