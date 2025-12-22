ALPHABET = "abcdefghijklmnopqrstuvwxyz"
REVERSED = ALPHABET[::-1]
ATBASH_TABLE = str.maketrans(ALPHABET, REVERSED)


def encode(plain_text):
    clean_text = "".join(c.lower() for c in plain_text if c.isalnum())
    substituted = clean_text.translate(ATBASH_TABLE)
    return " ".join(substituted[i : i + 5] for i in range(0, len(substituted), 5))


def decode(ciphered_text):
    clean_text = ciphered_text.replace(" ", "")
    return clean_text.translate(ATBASH_TABLE)
