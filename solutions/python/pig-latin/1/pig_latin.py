VOWELS = "aeiou"


def find_first_sound_index(word):
    if word[0] in VOWELS or word.startswith(("xr", "yt")):
        return 0

    for i, char in enumerate(word):
        # Règle 'qu' : si 'u' est précédé de 'q', on déplace le 'qu' entier.
        if char == "u" and i > 0 and word[i - 1] == "q":
            return i + 1

        # Règle 'y' comme voyelle (si non initial)
        if char == "y" and i > 0:
            return i

        # Règle de voyelle standard
        if char in VOWELS:
            return i

    return len(word)


def translate(text):
    # FIX: Gestion des phrases en divisant le texte en mots
    words = text.split()
    translated_words = []

    for word in words:
        vowel_sound_start_index = find_first_sound_index(word)

        head = word[vowel_sound_start_index:]
        tail = word[:vowel_sound_start_index]

        translated_words.append(head + tail + "ay")

    # FIX: Joindre les mots traduits en une phrase
    return " ".join(translated_words)
