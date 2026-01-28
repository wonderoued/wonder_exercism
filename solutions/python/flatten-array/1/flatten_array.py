def flatten(iterable):
    results = []
    for elements in iterable:
        if isinstance(elements, list):
            results.extend(flatten(elements))
        elif elements is not None:
            results.append(elements)
    return results
