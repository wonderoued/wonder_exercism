def rows(letter):
    target_index = ord(letter) - ord("A")
    size = 2 * target_index + 1
    result = []
    indices = list(range(target_index + 1)) + list(range(target_index -1, -1, -1))
    for i in indices:
        current_char = chr(ord("A") + i)
        row = [" "] * size
        row[target_index - i] = current_char
        row[target_index + i] = current_char
        result.append("".join(row))
    return result
