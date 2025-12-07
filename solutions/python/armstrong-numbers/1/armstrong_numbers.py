def is_armstrong_number(number):
    """determine if the given number is an armstrong's number
    :param number: int - the number to verify
    :return: bool - True is an armstrong's number, False if not"""
    str_number = str(number)
    num_digits = len(str_number)
    armstrong_sum = 0
    for digit_char in str_number:
        digit = int(digit_char)
        armstrong_sum += digit**num_digits
    return armstrong_sum == number
