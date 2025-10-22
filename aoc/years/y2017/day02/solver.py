import itertools


def part_one(input: str) -> str:
    number_lines = [
        [int(word) for word in line.split()] for line in input.strip().splitlines()
    ]
    checksum_sum = 0
    for numbers in number_lines:
        low, high = numbers[0], numbers[0]
        for value in numbers:
            if value < low:
                low = value
            if value > high:
                high = value
        checksum_sum += high - low
    return str(checksum_sum)


def part_two(input: str) -> str:
    number_lines = [
        [int(word) for word in line.split()] for line in input.strip().splitlines()
    ]
    checksum_sum = 0
    for numbers in number_lines:
        perms = itertools.permutations(numbers, 2)
        for perm in perms:
            if perm[0] * perm[1] == 0:
                raise SystemExit(
                    "I have not considered the case where any number pair is 0"
                )

            if perm[0] % perm[1] == 0:
                checksum_sum += perm[0] // perm[1]
    return str(checksum_sum)
