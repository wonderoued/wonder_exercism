def transform(legacy_data):
    new_data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            lowercase_letter = letter.lower()
            new_data[lowercase_letter] = score
    return new_data

# avec la comprehension de dictionnaire
# def transform(legacy_data):
    #return {
    #letter.lower(): score
    # for score, letters in legacy_data.items()
    #for letter in letters
#    }
