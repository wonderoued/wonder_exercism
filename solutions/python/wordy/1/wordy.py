def answer(question):
    content = question.removeprefix("What is").removesuffix("?").strip()
    if not content:
        raise ValueError("syntax error")

    content = content.replace("multiplied by", "multiplied")
    content = content.replace("divided by", "divided")
    tokens = content.split()

    try:
        result = int(tokens[0])
    except (ValueError, IndexError):
        raise ValueError("syntax error")

    i = 1
    while i < len(tokens):
        operation = tokens[i]
        if operation not in ["plus", "minus", "multiplied", "divided"]:
            if operation.isdigit() or (
                operation.startswith("-") and operation[1:].isdigit()
            ):
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        try:
            next_value = int(tokens[i + 1])
        except IndexError:
            raise ValueError("syntax error")
        except ValueError:
            raise ValueError("syntax error")
        if operation == "plus":
            result += next_value
        elif operation == "minus":
            result -= next_value
        elif operation == "multiplied":
            result *= next_value
        elif operation == "divided":
            result /= next_value

        i += 2
    return int(result)
