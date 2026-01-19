DATA = [
    ("house", "Jack built."),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),  # Attention: kissed, pas married
    ("priest all shaven and shorn", "married"),  # Attention: married, pas woke
    ("rooster that crowed in the morn", "woke"),  # Attention: woke, pas kept
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def recite(start_verse, end_verse):
    result = []
    for n in range(start_verse, end_verse + 1):
        verse = f"This is the {DATA[n-1][0]}"

        for i in range(n - 1, 0, -1):
            action = DATA[i][1]
            objet = DATA[i - 1][0]
            verse += f" that {action} the {objet}"

        verse += f" that {DATA[0][1]}"
        result.append(verse)
    return result
