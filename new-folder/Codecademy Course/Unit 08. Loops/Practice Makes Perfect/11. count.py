def count(sequence, item):
    result = 0
    for n in sequence:
        if n == item:
            result += 1
    return result
