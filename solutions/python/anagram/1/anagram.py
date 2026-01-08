def find_anagrams(word, candidates):
    target = word.lower()
    target_sorted = sorted(target)
    result = []
    for candidat in candidates:
        candidat_lower = candidat.lower()
        if candidat_lower == target:
            continue
        if sorted(candidat_lower) == target_sorted:
            result.append(candidat)

    return result
