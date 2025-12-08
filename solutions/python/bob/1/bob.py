def response(sentence):
    # D'abord, nettoyer la phrase des espaces pour vérifier le Silence et la Question
    # On garde l'originale pour le Hurlement, car les espaces comptent dans la condition isupper()
    stripped_sentence = sentence.strip()

    # --- 1. Vérification du Silence ---
    if not stripped_sentence:
        return "Fine. Be that way!"

    # --- Outils de vérification complexes ---
    # Pour le Hurlement, on doit vérifier si:
    # 1. Il y a au moins une lettre
    # 2. Toutes les lettres sont en majuscules
    is_shouting = sentence.isupper()

    # Pour la Question, on doit vérifier si la version nettoyée se termine par '?'
    is_question = stripped_sentence.endswith('?')

    # --- 2. Vérification de la Question Hurlée --- (La plus spécifique)
    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"

    # --- 3. Vérification du Hurlement --- (Seulement si ce n'est pas une question)
    elif is_shouting:
        return "Whoa, chill out!"

    # --- 4. Vérification de la Question --- (Seulement si ce n'est pas un hurlement)
    elif is_question:
        return "Sure."

    # --- 5. Cas par Défaut (Déclaration normale) ---
    else:
        return "Whatever."