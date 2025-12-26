from typing import NamedTuple


class ValueAndIndex(NamedTuple):
    value: int
    i: int


def get_highest(s: str, max_allowed_index: int, after_index: int) -> ValueAndIndex:
    high_value = -1
    high_index = 0
    for i, c in enumerate(s[after_index + 1 : max_allowed_index + 1]):
        if int(c) > high_value:
            high_value = int(c)
            high_index = i
    return ValueAndIndex(high_value, after_index + 1 + high_index)


def part_one(input: str) -> str:
    result = 0
    for line in input.strip().splitlines():
        first_digit, first_index = get_highest(
            line,
            max_allowed_index=len(line) - 2,
            after_index=-1,
        )
        second_digit, _ = get_highest(
            line,
            max_allowed_index=len(line) - 1,
            after_index=first_index,
        )
        result += first_digit * 10 + second_digit
    return str(result)


# same logic but 12 digits
def part_two(input: str) -> str:
    result = 0
    for line in input.strip().splitlines():
        # abcdefghijklmnopqrstuvwxyz
        #                          ^ len(s) - 1
        #               ^ len(s) - 12
        #               opqrstuvwxyz (12 digits)
        max_allowed_index = len(line) - 12
        line_result = 0
        exponent = 11
        after_index = -1
        while exponent >= 0:
            digit, after_index = get_highest(line, max_allowed_index, after_index)
            max_allowed_index += 1
            line_result += digit * pow(10, exponent)  # pyright: ignore[reportAny]
            exponent -= 1
        result += line_result
    return str(result)
