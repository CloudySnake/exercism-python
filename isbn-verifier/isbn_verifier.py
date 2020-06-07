def validate_character(char: str, multi: int):
    if char == "X" and multi == 1:
        return 10
    return int(char) * multi


def is_valid(isbn):
    isbn = isbn.replace("-", "")

    try:
        digits = [validate_character(char, 10 - pos) for pos, char in enumerate(isbn)]
    except ValueError:
        return False
    return sum(digits) % 11 == 0 if len(digits) == 10 else False
