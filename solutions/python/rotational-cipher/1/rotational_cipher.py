def rotate(text, key):
    result = ""
    for char in text:
        if "a" <= char <= "z":
            # Minuscules : a=0, b=1, ..., z=25
            base = ord("a")
            old_index = ord(char) - base
            new_index = (old_index + key) % 26
            new_char = chr(new_index + base)
            result += new_char
        elif "A" <= char <= "Z":
            # Majuscules : A=0, B=1, ..., Z=25
            base = ord("A")
            old_index = ord(char) - base
            new_index = (old_index + key) % 26
            new_char = chr(new_index + base)
            result += new_char
        else:
            # Conserver les autres caractères (espaces, ponctuation, nombres)
            result += char
    return result
