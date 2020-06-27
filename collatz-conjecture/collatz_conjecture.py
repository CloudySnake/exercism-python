def process_step(num: int) -> int:
    if num % 2 == 0:
        return num // 2
    return num * 3 + 1


def steps(number: int) -> int:
    step_count = 0
    if number <= 0:
        raise ValueError("Value must be positive")
    while number != 1:
        number = process_step(number)
        step_count += 1
    return step_count
