def is_valid(isbn):
    isbn_cleaned = isbn.replace("-", "")

    if len(isbn_cleaned) != 10:
        return False

    total_sum = 0

    for i, char in enumerate(isbn_cleaned):
        weight = 10 - i

        if i < 9:
            if char.isdigit():
                digit_value = int(char)
            else:
                return False
        else:
            if char.isdigit():
                digit_value = int(char)
            elif char == "X":
                digit_value = 10
            else:
                return False

        total_sum += digit_value * weight

    return total_sum % 11 == 0
